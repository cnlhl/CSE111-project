from django.urls import path
from .views import user_login
from . import views

urlpatterns = [
    # 其他 URL 模式
    path('api/login', user_login, name='login'),
    path('users/<int:user_id>/', views.get_user_data, name='get_user_data'),
]

"""
URL configuration for meetminder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meetings.urls')),  # 包含 'meetings' 应用的 URL
]

