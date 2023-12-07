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
    user_data = test_attendee_read()
    if user_data:
        return JsonResponse(user_data)
    else:
        return JsonResponse({'error': 'User not found'}, status=404)
    
def process_user_data(user_id):
    try:
        # 假设 userid 是 User 模型的字段
        user = User.objects.get(userid=user_id)  # 获取 User 实例
        meetings_attended = Attendee.objects.filter(user=user)  # 获取该用户的参会信息
        notifications = Notification.objects.filter(user=user)  # 获取该用户的通知
        
        # 构建响应数据
        user_data = {
            'username': user.username,
            'meetings_attended': list(meetings_attended.values('meeting_id', 'status')),
            'notifications': list(notifications.values('message', 'timestamp'))  # 添加通知数据
        }
        return user_data
    except User.DoesNotExist:
        # 处理用户不存在的情况
        return None
    
def test_attendee_read():
    # 查询所有的Attendee记录
    attendees = Attendee.objects.all()

    # 创建一个包含所有Attendee信息的列表
    attendees_data = [{"username": attendee.user.username, "meeting_title": attendee.meeting.title, "status": attendee.status} for attendee in attendees]

    # 将数据返回为JSON响应
    return JsonResponse(attendees_data, safe=False)