from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
# CRUD For User
def create_user(request):
    if request.method == 'POST':
        # Handle Request Data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create New User Object
        new_user = User(username=username, email=email, password=password)

        # Save New User into Database
        new_user.save()

        return HttpResponse("User created successfully!", status=201)
    else:
        return HttpResponse("Invalid Request Method!", status=400)
    
def signin_user(request):
    if request.method == 'POST':
        # Handle Request Data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Get user from the database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        # Check if the retrieved user has the same password
        if user is not None and user.password == password:
            return JsonResponse({'success': True, 'message': 'User authenticated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)
    else:
        return HttpResponse("Invalid Request Method!", status=400)
  
def test_user():
    print("Hello World!")
    pass
