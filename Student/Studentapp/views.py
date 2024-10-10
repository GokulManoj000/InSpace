from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .models import HomeworkFile  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    return render(request, 'Student/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            msg = 'username already exists!'
            return render(request, 'Student/register.html',{'msg':msg})
        else:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            User.objects.create(username=username,email=email,password=password,first_name=name)
            user1=User.objects.filter(username=username,password=password,email=email)
            for i in user1:
                if i.username==username:
                    user=i.id
                    break
            user = User.objects.get(id=user)
            
            return redirect('index')
            
    return render(request, 'Student/register.html')

def stud_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        # if user is not None and user.is_active:
        #     if user.is_superuser==False and user.is_staff==False:
        #         login(request,user)
        #         return redirect('userprofile')
        #     elif user.is_superuser==False and user.is_staff==False:
        #         login(request,user)
        return redirect('dashboard')
        # elif user is None:
        #     msg = "Wrong credentials. Please try again!"
        #     return render(request , 'Student/stud_login.html' , {'msg':msg})
    return render(request , 'Student/stud_login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def dashboard_view(request):
    return render(request, 'Student/dashboard.html')



def dashboard_view(request):
    homework_files = HomeworkFile.objects.filter(user=request.user.id)  # Fetch user-specific homework files
    return render(request, 'Student/dashboard.html', {'homework_files': homework_files})


def submit_homework(request):
    if request.method == 'POST':
        homework_file = request.FILES.get('homework_file')
        # Create a HomeworkFile instance (you need to implement the model)
        HomeworkFile.objects.create(user=request.user.id, file=homework_file)
        return redirect('dashboard')  # Redirect back to dashboard after submission


def delete_homework(request):
    if request.method == 'POST':
        homework_file_id = request.POST.get('homework_file_id')
        try:
            homework_file = HomeworkFile.objects.get(id=homework_file_id, user=request.user)
            homework_file.delete()  # Delete the selected homework file
        except HomeworkFile.DoesNotExist:
            pass
        return redirect('dashboard')  # Redirect back to dashboard after deletion