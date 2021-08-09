from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', views.logout_view, name='logout'),
    # path('edit/', views.edit, name='edit_account'),
]