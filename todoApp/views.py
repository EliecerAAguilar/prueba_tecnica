from django.shortcuts import render, redirect
from .models import task

# Create your views here.

def list_tasks(request):
    return render(request, 'list_tasks.html')

def create_tasks(request):
    tasks = task(title=request.POST['form_title'], description=request.POST['form_description'])
    tasks.save()
    return redirect('/tasks/')
