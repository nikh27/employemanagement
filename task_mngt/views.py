from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import *
from .forms import *
# Create your views here.

def task_management(request):
    return render(request,'task_management.html')

def milestone(request):
    milestones = Milestone.objects.all()

    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Milestone added successfully!')
            return redirect('milestone')
        else:
            messages.error(request, 'Failed to add milestone. Check form errors.')

    form = MilestoneForm()
    return render(request, 'milestone.html', {'milestones': milestones, 'form': form})

def delete_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id)
    milestone.delete()
    return redirect('milestone')

def edit_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id)

    if request.method == 'POST':
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('milestone')
    else:
        form = MilestoneForm(instance=milestone)
    form = MilestoneForm()
    return render(request, 'edit_milestone.html', {'form': form, 'milestone': milestone})

def delete_task(request, task_id):
    work_item = get_object_or_404(WorkItem, id=task_id)
    work_item.delete()
    return redirect('create_task')

def create_task(request):
    workitems = WorkItem.objects.all()
    form = WorkItemForm()

    if request.method == 'POST':
        form = WorkItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('create_task')
        else:
            messages.error(request, 'Failed to add task. Check form errors.')
    return render(request,'create_task.html', {"workitems": workitems,"form":form})

def edit_task(request, task_id):
    task = get_object_or_404(WorkItem, id=task_id)

    if request.method == 'POST':
        form = WorkItemForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('create_task') 
    else:
        form = WorkItemForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})

def update_assign(request, assignment_id):
    assign = get_object_or_404(TaskAssignment, id=assignment_id)

    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST, instance=assign)
        if form.is_valid():
            form.save()
            return redirect('assign_task') 
    else:
        form = TaskAssignmentForm(instance=assign)

    return render(request, 'update_assign.html', {'form': form, 'assign': assign})

def assign_task(request):
    assign_task = TaskAssignment.objects.all()
    form = TaskAssignmentForm()

    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'assign successfully!')
            return redirect('assign_task')
        else:
            messages.error(request, 'Failed to assign task. Check form errors.')

    return render(request,'assign_task.html',{'assign_task':assign_task, "form":form})

def delete_assignment(request, assignment_id):
    task = get_object_or_404(TaskAssignment, id=assignment_id)
    task.delete()
    return redirect('assign_task')

def my_task(request):
    return render(request,'my_task.html')