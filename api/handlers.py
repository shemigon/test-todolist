from piston.handler import BaseHandler
from piston.utils import rc
from todo.forms import TaskForm
from todo.models import Task


class TaskHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    model = Task
    fields = ('id', 'name', 'priority')

    def read(self, request, task_id=None):
        base = Task.objects
        return (base.get(pk=task_id)
                if task_id else base.filter(user=request.user))

    def create(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            task = form.save()
            return task
        return rc.BAD_REQUEST

    def update(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id, user=request.user)
        except Task.DoesNotExist:
            return rc.NOT_FOUND
        form = TaskForm(request.PUT, instance=task)
        if form.is_valid():
            task = form.save()
            return task
        return rc.BAD_REQUEST

    def delete(self, request, task_id):
        try:
            Task.objects.get(pk=task_id, user=request.user).delete()
        except Task.DoesNotExist:
            return rc.NOT_FOUND
        return rc.DELETED
