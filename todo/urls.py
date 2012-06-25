from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('todo.views',
    url(r'^$', 'task_list_view', name='task_list'),
    url(r'^add/$', 'task_add_view', name='task_add'),
    url(r'^edit/(?P<task_id>\d+)/$', 'task_edit_view', name='task_edit'),
    url(r'^delete/(?P<task_id>\d+)$', 'task_delete_view', name='task_delete'),
)
