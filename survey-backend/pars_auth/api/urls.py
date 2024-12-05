from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = "auth_api"

urlpatterns = [
    path('user/', views.GetLoginUserAPIView.as_view(), name='user'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('confirmation/<token>/', views.ConfirmUser.as_view(), name='confirmation'),
    path('password_reset/', views.PasswordResetTokenManageView.as_view(), name='password_reset'),
    path('login_with_token/', views.LoginWithToken.as_view(), name='login_with_token'),
    path('token/', views.EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

