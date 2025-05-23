"""
URL configuration for djlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.homepage, name="homepage"),
    path("post/<int:post_id>/", blog.views.post),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html", next_page="homepage")),
    path("logout/", blog.views.logout),
    path("signup/", blog.views.signup),
]
