from django import forms
from django.conf import settings
from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user',)
        widgets = {
            'priority': forms.Select(choices=((i, i)
                for i in xrange(1, settings.MAX_PRIORITY + 1)))
        }
