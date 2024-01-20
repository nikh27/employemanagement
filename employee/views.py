from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import HttpResponseBadRequest
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

@login_required
def user_management(request):
    return render(request, 'user_management.html')

@login_required
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

@login_required
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
            return redirect('department') 
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'edit_department.html', {'department': department, 'form': form})

@login_required
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

@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')  # Redirect to the department list or any other page
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})

@login_required
def report(request):
    return render(request, 'report.html')

@login_required
def user_master(request):
    is_staff_user = request.user.is_staff
    if is_staff_user:
        users = EmployeeDetail.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'user_master.html', context)
    else:
        user = get_object_or_404(EmployeeDetail, user=request.user)
        return render(request, 'view_user.html', {'user': user})

@login_required
def department(request):
    is_staff_user = request.user.is_staff
    if is_staff_user:
        departments = Department.objects.all()
        return render(request, 'department.html', {'departments': departments})
    else:
        employee_detail = get_object_or_404(EmployeeDetail, user=request.user)
        department = employee_detail.empdept
        return render(request, 'view_department.html', {'department': department})

@login_required
def designations(request):
    is_staff_user = request.user.is_staff
    if is_staff_user:
        designations = Designation.objects.all()
        return render(request, 'designation.html', {'designations': designations})
    else:
        employee_detail = get_object_or_404(EmployeeDetail, user=request.user)
        designation = employee_detail.designation
        return render(request, 'view_designation.html', {'designation': designation})

def view_designation(request, designation_id):
    designation = get_object_or_404(Designation, id=designation_id)
    return render(request, 'view_designation.html', {'designation': designation})

def add_designation(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('designations')
    else:
        form = DesignationForm()

    return render(request, 'add_designation.html', {'form': form})

def edit_designation(request, designation_id):
    designation = get_object_or_404(Designation, id=designation_id)

    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            form.save()
            return redirect('designations')
    else:
        form = DesignationForm(instance=designation)

    return render(request, 'edit_designation.html', {'form': form, 'designation': designation})

def delete_designation(request, designation_id):
    designation = get_object_or_404(Designation, id=designation_id)

    if request.method == 'POST':
        designation.delete()
        return redirect('designations')

    return render(request, 'delete_designation.html', {'designation': designation})

@login_required
@user_passes_test(lambda u: u.is_staff)
def user_menu_permission(request):
    permissions = UserMenuPermission.objects.all()
    return render(request, 'user_menu_permission.html', {'permissions': permissions})

@login_required
def update_permission(request, permission_id):
    permission = get_object_or_404(UserMenuPermission, id=permission_id)
    
    if request.method == 'POST':
        new_permission_level = request.POST.get('new_permission_level')
        if new_permission_level != '':
            permission.permission_level = new_permission_level
            permission.save()
        else:
            return HttpResponseBadRequest("<h1>Please select a any permission level</h1>")

    return redirect('user_menu_permission')
