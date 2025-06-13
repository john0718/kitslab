from django.urls import path
from . import views

urlpatterns = [
    path('reset_ldap_password/', views.ldap_reset_request_view, name='ldap_reset_request'),

    path('reset_ldap_password/<str:token>/', views.ldap_reset_confirm_view, name='ldap_reset_confirm'),
    path('check-ldap/', views.check_ldap_type, name='check_ldap'),
    path('ldap-lookup/', views.ldap_user_lookup_view, name='ldap_lookup'),

    
]


