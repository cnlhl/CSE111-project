from meetings.models import User

# 批量导入40条数据
for i in range(1, 41):
    username = f'user{i}'
    email = f'user{i}@example.com'
    password = f'password{i}'
    
    # 创建并保存用户对象
    user = User(username=username, email=email, password=password)
    user.save()

print("导入数据完成")
