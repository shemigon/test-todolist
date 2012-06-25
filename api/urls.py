from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import TaskHandler

auth = HttpBasicAuthentication(realm="Test Todo List")
task_handler = Resource(TaskHandler, authentication=auth)

urlpatterns = patterns('',
   url(r'^task/(?P<task_id>\d+)/', task_handler),
   url(r'^task/', task_handler),
)
