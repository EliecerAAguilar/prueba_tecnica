from django.shortcuts import render, redirect
from .models import task

# Create your views here.

def list_tasks(request):
    tasks = task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_tasks(request):
    tasks = task(title=request.POST['form_title'], description=request.POST['form_description'])
    tasks.save()
    return redirect('/')

def delete_task(request, task_id):
    deleted_task = task.objects.get(id=task_id)
    deleted_task.delete()
    return redirect('/')

def update(request, task_id):
    update_task = task.objects.get(id=task_id)
    return render(request, "update.html", {"task": update_task})

def updated_task(request, task_id):
    title = request.POST['form_title']
    description = request.POST['form_description']
    update = task.objects.get(id=task_id)
    update.title = title
    update.description = description
    update.save()
    return redirect('/')

