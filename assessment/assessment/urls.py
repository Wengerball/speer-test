"""
URL configuration for assessment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from notes.api.notes import NoteViewSet, NoteSearch
from notes.api.user import SignupView, LoginView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/search', NoteSearch.as_view(), name='note-search'),
    path('api/auth/signup', SignupView.as_view(), name='auth-signup'),
    path('api/auth/login', LoginView.as_view(), name='auth-login'),
]
