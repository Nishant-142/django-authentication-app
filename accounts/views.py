from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User

# role check functions
def is_admin(user):
    return user.is_authenticated and user.is_superuser
def is_user(user):
    return user.is_authenticated and not user.is_superuser and user.is_approved

# create you views here
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            
            elif user.is_approved:
                login(request, user)
                return redirect('user_dashboard')
            
            else:
                messages.error(request, "Your account is not approved by admin")
                logout(request)
                return redirect('login')
            
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'admin_dashboard.html', {'users' : users})

@login_required(login_url='login')
@user_passes_test(is_user, login_url='login')
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    
    if request.method == "POST":
    #    user = get_object_or_404(User,id=id)
    #    user.username = request.POST.get('confirm_delete.html')
       user.delete()
       return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'user':user})

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def approve_user(request, id):
    if request.method == "POST":
      user = get_object_or_404(User, id=id)
      user.is_approved = True
      user.save()
    return redirect('admin_dashboard')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def update_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('admin_dashboard')
    
    return render(request, 'update_user.html',{'user':user})