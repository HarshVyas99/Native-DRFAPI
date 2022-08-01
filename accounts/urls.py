from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views


urlpatterns = [
    path('signup/', views.Signup.as_view(), name='accounts-signup'),
    path('signup/verify/', views.SignupVerify.as_view(),
         name='accounts-signup-verify'),

    path('login/', views.Login.as_view(), name='accounts-login'),
    path('logout/', views.Logout.as_view(), name='accounts-logout'),

    path('password/reset/', views.PasswordReset.as_view(),
         name='accounts-password-reset'),
    path('password/reset/verify/', views.PasswordResetVerify.as_view(),
         name='accounts-password-reset-verify'),
    path('password/reset/verified/', views.PasswordResetVerified.as_view(),
         name='accounts-password-reset-verified'),

    path('email/change/', views.EmailChange.as_view(),
         name='accounts-email-change'),
    path('email/change/verify/', views.EmailChangeVerify.as_view(),
         name='accounts-email-change-verify'),

    path('password/change/', views.PasswordChange.as_view(),
         name='accounts-password-change'),

    path('users/me/', views.UserMe.as_view(), name='accounts-me'),
]


urlpatterns = format_suffix_patterns(urlpatterns)