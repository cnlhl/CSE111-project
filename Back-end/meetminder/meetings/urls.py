from django.urls import path
from .views import user_login
from . import views

urlpatterns = [
    # 其他 URL 模式
    path('api/login', user_login, name='login'),
]