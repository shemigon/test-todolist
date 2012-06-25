from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from todo.forms import TaskForm
from todo.models import Task


@login_required
@render_to('todo/task_list.html')
def task_list_view(request):
    return {
        'tasks': Task.objects.filter(user=request.user)
    }


@login_required
@render_to('todo/task_add_edit.html')
def task_add_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(task_list_view)
    else:
        form = TaskForm()
    return {
        'form': form,
        'action': 'add',
    }


@login_required
@render_to('todo/task_add_edit.html')
def task_edit_view(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(task_list_view)
    else:
        form = TaskForm(instance=task)
    return {
        'form': form,
        'action': 'edit',
    }


@login_required
@render_to('todo/')
def task_delete_view(request, task_id):
    get_object_or_404(Task, pk=task_id, user=request.user).delete()
    return redirect(task_list_view)
