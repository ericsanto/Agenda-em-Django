from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name ='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logouth.html' ), name='logout'),
]
