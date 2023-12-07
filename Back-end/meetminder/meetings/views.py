from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .models import User, Meeting, Agenda, Attendee, Notification, Resource, Room
import json

def user_login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username, password)

        user = User.objects.filter(username=username, password=password).first()
        print(user.id)
        if user:
            # 用户名和密码匹配
            print("user login success")
            return JsonResponse({'success': True, 'userid': user.userid, 'username': user.username})
        else:
            # 用户名或密码错误
            print("user login failed")
            return JsonResponse({'success': False, 'message': 'Invalid username or password'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})