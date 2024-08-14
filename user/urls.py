from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


from . import views

app_name = 'api_user'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='api_login'),
]