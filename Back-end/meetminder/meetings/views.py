from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .models import User, Meeting, Agenda, Attendee, Notification, Resource, Room
import json

@require_http_methods(["POST"])
def user_login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username, password=password).first()
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

def get_user_data(request, user_id):
    user_data = process_user_data(user_id)
    if user_data:
        return JsonResponse(user_data)
    else:
        return JsonResponse({'error': 'User not found'}, status=404)
    
def process_user_data(user_id):
    try:
        user = User.objects.get(userid=user_id)
        meetings_attended = Meeting.objects.filter(attendeeid=user.userid)
        notifications = Notification.objects.filter(userid=user.userid)
        
        # 构建响应数据
        user_data = {
            'username': user.username,
            'meetings_attended': list(meetings_attended.values()),
            'notifications': list(notifications.values())
        }
        
        return user_data
    except User.DoesNotExist:
        # 处理用户不存在的情况
        return None