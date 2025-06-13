
# Replace with your actual LDAP config
# LDAP_SERVER = 'ldap://zion.karunya.edu'
# LDAP_BASE_DN = 'CN=ubuntu,CN=users,DC=karunya,DC=edu'
# LDAP_USER_FILTER = '(mail={})'





from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.core.cache import cache
from .forms import LdapPasswordResetRequestForm, LdapSetPasswordForm
import base64
import ldap3
import os
import logging
from datetime import datetime
from .models import PasswordResetLog
from django.http import JsonResponse
from django.conf import settings

signer = TimestampSigner()
password_reset_logger = logging.getLogger("ldap_password_reset")

# Load LDAP env vars
TEST_LDAP_SERVER_URI = os.getenv('TEST_LDAP_SERVER_URI')
TEST_LDAP_BIND_DN = os.getenv('TEST_LDAP_BIND_DN')
TEST_LDAP_BIND_PASSWORD = os.getenv('TEST_LDAP_BIND_PASSWORD')
TEST_LDAP_SEARCH_BASE = os.getenv('TEST_LDAP_SEARCH_BASE')


def ldap_user_exists(email):
    server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI,use_ssl=True)
    conn = ldap3.Connection(
        server,
        user=settings.AUTH_LDAP_BIND_DN,
        password=settings.AUTH_LDAP_BIND_PASSWORD,
    )
    conn.bind() 
    print("Connecting to:", settings.AUTH_LDAP_SERVER_URI)
    


    if not conn.bind():
        print("Bind failed:", conn.result)
        raise Exception("LDAP bind failed")

    conn.search(
        search_base=TEST_LDAP_SEARCH_BASE,
        search_filter=f"(mail={email})",
        attributes=['mail', 'uid', 'cn', 'distinguishedName']
    )

    return conn.entries[0] if conn.entries else None


def send_reset_email(email, token, request):
    encoded_token = base64.urlsafe_b64encode(token.encode()).decode()
    reset_link = f"{request.scheme}://{request.get_host()}/ctc_seraphauthentication/reset_ldap_password/{encoded_token}/"
    try:
        send_mail(
            subject="Seraph Password Reset",
            message=f"Click the link to reset your password: {reset_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
    except Exception as e:
        password_reset_logger.error(f"Failed to send reset email to {email}: {e}")
        raise    


def ldap_reset_request_view(request):
    message = None 
    if request.method == "POST":
        form = LdapPasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = ldap_user_exists(email)
            if user:
                token = signer.sign(email)
                send_reset_email(email, token, request)
                message = "A password reset link has been sent to your email."
            else:
                form.add_error('email', 'Invalid Username and Password')
    else:
        form = LdapPasswordResetRequestForm()
    return render(request, 'ldap_reset_request.html', {
        'form': form,
        'message': message,
    })


def ldap_reset_confirm_view(request, token):
    message = None
    # user_dn = None  # ✅ Ensure this is defined before the try block

    try:
        decoded_token = base64.urlsafe_b64decode(token.encode()).decode()
        email = signer.unsign(decoded_token, max_age=300)  # Token expires in 5 minutes
    except (SignatureExpired, BadSignature, Exception):
        return render(request, 'ldap_reset_confirm.html', {
            'error': 'Invalid or expired link'
        })

    if request.method == "POST":
        form = LdapSetPasswordForm(request.POST)
        if form.is_valid():
            # old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password1']

            try:
                # Step 1: Search for user_dn using a service/bind account
                search_server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI, use_ssl=True)
                search_conn = ldap3.Connection(
                    search_server,
                    user=settings.AUTH_LDAP_BIND_DN,
                    password=settings.AUTH_LDAP_BIND_PASSWORD,
                    auto_bind=True
                )
                search_conn.search(
                    search_base=os.getenv('TEST_LDAP_SEARCH_BASE', "DC=karunya,DC=edu"),
                    search_filter=f"(mail={email})",
                    attributes=["distinguishedName"]
                )

                if not search_conn.entries:
                    PasswordResetLog.objects.create(
                        email=email,
                        user_dn="Not Found",
                        status="Failed - User Not Found",
                        ip_address=request.META.get('REMOTE_ADDR')
                    )
                    return render(request, 'ldap_reset_confirm.html', {
                        'form': form,
                        'error': 'LDAP user not found'
                    })

                user_dn = search_conn.entries[0].entry_dn
                print(f"Found DN: {user_dn}")

                # Step 2: Rebind using the user's DN and old password
                user_conn = ldap3.Connection(
                    search_server,
                    user=settings.AUTH_LDAP_BIND_DN,
                    password=settings.AUTH_LDAP_BIND_PASSWORD,
                    auto_bind=True
                )

                # Step 3: Attempt password change using Microsoft's password extension
                success = user_conn.extend.microsoft.modify_password(
                    user=user_dn,
                    new_password=new_password
                )

                PasswordResetLog.objects.create(
                    email=email,
                    user_dn=user_dn,
                    status="Success" if success else "Failed",
                    ip_address=request.META.get('REMOTE_ADDR')
                )

                if success:
                    message = "Password has been reset successfully."
                    form = None
                else:
                    return render(request, 'ldap_reset_confirm.html', {
                        'form': form,
                        'error': f"Password update failed: {user_conn.result.get('message') or user_conn.result}"
                        
                    })

            except Exception as e:
                PasswordResetLog.objects.create(
                    email=email,
                    user_dn=user_dn or "Unknown",
                    status="Failed - Exception",
                    ip_address=request.META.get('REMOTE_ADDR')
                )
                return render(request, 'ldap_reset_confirm.html', {
                    'form': form,
                    'error': f'Error updating password: {str(e)}'
                })
    else:
        form = LdapSetPasswordForm()

    return render(request, 'ldap_reset_confirm.html', {
        'form': form,
        'message': message,
    })



def check_ldap_type(request):
    try:
        server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI)
        conn = ldap3.Connection(
            server,
            user=settings.AUTH_LDAP_BIND_DN,
            password=settings.AUTH_LDAP_BIND_PASSWORD,
            auto_bind=True
        )

        conn.search(
            search_base='DC=karunya,DC=edu',
            search_filter='(objectClass=*)',
            attributes=['vendorName', 'name', 'operatingSystem']
        )

        entries = [entry.entry_to_json() for entry in conn.entries]
        return JsonResponse({"entries": entries})

    except Exception as e:
        return JsonResponse({"error": str(e)})
    




from django.shortcuts import render
from django.conf import settings
import ldap3

def ldap_user_lookup_view(request):
    context = {}

    if request.method == 'POST':
        email_to_search = request.POST.get('email')

        try:
            # Setup secure connection to LDAP
            server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI,use_ssl=True)   #use_ssl=True
            conn = ldap3.Connection(
                server,
                user=settings.AUTH_LDAP_BIND_DN,
                password=settings.AUTH_LDAP_BIND_PASSWORD,
                auto_bind=True
            )

            # Perform search
            conn.search(
                search_base="DC=karunya,DC=edu",
                search_filter=f"(mail={email_to_search})",
                attributes=["distinguishedName", "mail", "sAMAccountName", "cn"]
            )

            if conn.entries:
                entry = conn.entries[0]
                context['dn'] = entry.entry_dn
                context['attributes'] = entry.entry_attributes_as_dict
            else:
                context['error'] = "No LDAP user found for the given email."

        except Exception as e:
            context['error'] = f"LDAP error: {str(e)}"

    return render(request, 'ldap_user_lookup.html', context)

