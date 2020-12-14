from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request, "Task Added Successfully!!!")
        else:
            messages.success(request, "Enter Something...")
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)

    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, "Access Restricted, Not Allowed!!!")
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    task_obj = TaskList.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Edited!")
        else:
            messages.success(request, "Invalid Value!")
        return redirect('todolist')
    else:
        return render(request, 'edit.html', {'task_obj': task_obj})


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)

    if task.owner == request.user:
        if task.done == False:
            task.done = True
        else:
            task.done = False
        task.save()
    else:
        messages.error(request, "Access Restricted, Not Allowed!!!")

    return redirect('todolist')


def index(request):
    context = {
        'index_text': "Welcome to Index Page",
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        'contact_text': "Welcome to Contact Us Page",
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': "Welcome to About Us Page",
    }
    return render(request, 'about.html', context)
