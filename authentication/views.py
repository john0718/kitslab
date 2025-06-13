from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import UserProfile,Role



class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def get_success_url(self):
        # Prioritize redirection to ?next= if present
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        if next_url:
            return next_url

        user = self.request.user

        # Ensure user is authenticated
        if not user.is_authenticated:
            return reverse_lazy('login')

        # Create UserProfile if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={'role': Role.FACULTY if user.email.endswith('@karunya.edu') else 'UNKNOWN'}
        )

        # Redirect based on role
        if profile.role == Role.COORDINATOR:
            return reverse_lazy('faculty_dashboard')
        elif profile.role == Role.FACULTY or user.email.endswith('@karunya.edu'):
            return reverse_lazy('faculty_lab_requests')

        # Fallback
        return reverse_lazy('login')




# class CustomLoginView(LoginView):
#     template_name = 'authentication/login.html'

#     def get_success_url(self):
#         user = self.request.user

#         # Ensure user is authenticated
#         if not user.is_authenticated:
#             return reverse_lazy('login')

#         # Create UserProfile if it doesn't exist
#         profile, created = UserProfile.objects.get_or_create(
#             user=user,
#             defaults={'role': Role.FACULTY if user.email.endswith('@karunya.edu') else 'UNKNOWN'}
#         )

#         # Redirect based on role
#         if profile.role == Role.COORDINATOR:
#             return reverse_lazy('faculty_dashboard')
#         elif profile.role == Role.FACULTY or user.email.endswith('@karunya.edu'):
#             return reverse_lazy('faculty_lab_requests')

#         # Fallback
#         return reverse_lazy('login')