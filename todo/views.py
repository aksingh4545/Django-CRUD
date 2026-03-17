
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(task=task)
    return redirect('task_list')


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('task_list')