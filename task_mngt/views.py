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
            return redirect('milestone')  # Redirect to the appropriate URL after editing
    else:
        form = MilestoneForm(instance=milestone)

    return render(request, 'edit_milestone.html', {'form': form, 'milestone': milestone})

def create_task(request):
    workitems = WorkItem.objects.all()
    return render(request,'create_task.html', {"workitems": workitems})

def assign_task(request):
    assign_task = TaskAssignment.objects.all()
    return render(request,'assign_task.html',{'assign_task':assign_task})

def my_task(request):
    return render(request,'my_task.html')