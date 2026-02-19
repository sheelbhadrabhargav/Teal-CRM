from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/lead/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('about/',about, name='about' ),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
]
