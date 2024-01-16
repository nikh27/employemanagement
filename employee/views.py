from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def registration(request):
    error = ''
    if request.method == 'POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ec = request.POST.get('empcode')
        em = request.POST.get('email')
        pwd = request.POST.get('password')

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user=user, empcode=ec)
            error = 'no'
        except Exception as e:
            # Debugging: Print the exception message
            print(f'Error: {e}')
            error = 'yes'


    return render(request, 'registration.html', locals())

def emp_login(request):
    error = ''
    if request.method == 'POST':
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        user = authenticate(username=em, password=pwd)
        if user:
            login(request, user)
            error = 'no'
        else:
            error = 'yes'
    return render(request, 'emp_login.html',locals())

def Logout(request):
    logout(request)
    return redirect("index")

@login_required(login_url='emp_login')
def admin_log(request):
    error = ''
    if request.method == 'POST':
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        user = authenticate(username=em, password=pwd)
        if user is not None and user.is_staff:
            login(request, user)
            error = 'no'
        else:
            error = 'yes'
    return render(request, 'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def user_management(request):
    return render(request, 'user_management.html')


def edit_user(request, user_id):
    user = get_object_or_404(EmployeeDetail, id=user_id)
    
    if request.method == 'POST':
        form = EmployeeDetailForm(request.POST, instance=user)
        user_form = UserForm(request.POST, instance=user.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect('user_master') 
    else:
        form = EmployeeDetailForm(instance=user)
        user_form = UserForm(instance=user.user)

    return render(request, 'edit_user.html', {'user': user, 'form': form, 'user_form': user_form})

def view_user(request, user_id):
    user = get_object_or_404(EmployeeDetail, id=user_id)
    return render(request, 'view_user.html', {'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(EmployeeDetail, id=user_id)

    if request.method == 'POST':
        # Delete user and associated EmployeeDetail
        user.delete()
        return redirect('user_master')  # Redirect to a success page or wherever you want

    return render(request, 'delete_user.html', {'user': user})

@login_required
def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department')  # Redirect to the department page
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'edit_department.html', {'department': department, 'form': form})

def view_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return render(request, 'view_department.html', {'department': department})

@login_required
def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        # Delete department
        department.delete()
        return redirect('department')  # Redirect to a success page or wherever you want

    return render(request, 'delete_department.html', {'department': department})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')  # Redirect to the department list or any other page
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})

def task_management(request):
    return render(request, 'task_management.html')

def report(request):
    return render(request, 'report.html')

def user_master(request):
    
    users = EmployeeDetail.objects.all()
    context = {'users': users}
    return render(request, 'user_master.html', context)

def department(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})

def designation(request):
    designations = Designation.objects.all()
    return render(request, 'designation.html', {'designations': designations})

def user_menu_permission(request):
    permissions = UserMenuPermission.objects.all()
    return render(request, 'user_menu_permission.html', {'permissions': permissions})