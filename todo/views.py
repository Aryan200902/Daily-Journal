from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request,'login.html')

@login_required(login_url='user_login')
def home(request):
    return render(request,'index.html')
    
@login_required(login_url='user_login')
def submit(request):
    obj=Todo()
    obj.title = request.POST.get('title')
    obj.description = request.POST.get('description')
    obj.user = request.user
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.filter(user=request.user)
    }
    return redirect('list')

@login_required(login_url='user_login')
def delete(request,id):
    #Use get_object_or_404 to get the Todo object or return a 404 response
    todo_obj = get_object_or_404(Todo, id=id, user=request.user)
    todo_obj.delete()
    mydictionary = {
        "alltodos": Todo.objects.filter(user=request.user)
    }
    messages.success(request,"Task Deleted Successfully.")
    return redirect('list')

@login_required(login_url='user_login')
def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.filter(user=request.user)
    }
    return render(request,'list.html',context=mydictionary)

@login_required(login_url='user_login')
def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "id" : obj.id,
        "alltodos": Todo.objects.filter(user=request.user)
    }
    return render(request,'edit.html',context=mydictionary)

@login_required(login_url='user_login')
def update(request, id):
    obj = Todo.objects.get(id=id)
    if request.method=='POST':
        obj.title = request.POST.get('title')
        obj.description = request.POST.get('description')
        import datetime
        updated_at = datetime.datetime.now()
        obj.created_at = updated_at
        obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.filter(user=request.user)
    }
    return render(request, 'list.html', context=mydictionary)

@login_required(login_url='user_login')
def delete_all(request):
    Todo.objects.filter(user=request.user).delete()
    return redirect('list')

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            
            login(request,user)
            messages.success(request,'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'login.html')

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('create_user')  # Redirect back to the same page

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('create_user')  # Redirect back to the same page

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('create_user')  # Redirect back to the same page

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.is_superuser = True
        user.save()
        messages.success(request, "User created successfully.")
        return redirect('login')  # Redirect to login page after successful user creation

    return render(request, 'signup.html')  # Render the template for user creation form
        
@login_required(login_url='user_login')
def logoutuser(request):
    logout(request)
    return redirect('user_login')