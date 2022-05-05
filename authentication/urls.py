from django.urls import path
from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView, LoginView, LogoutView, RequestPasswordResetEmail, CompletePasswordReset
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name="validate-email"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('request-password', RequestPasswordResetEmail.as_view(), name='request-password'),
    path('set-new-password/<uidb64>/<token>', CompletePasswordReset.as_view(),
         name='reset-user-password'),
]
