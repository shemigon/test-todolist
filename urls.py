from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
from registration.views import register
from django.views.generic.simple import direct_to_template


admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^api/', include('api.urls')),

    url(r'^', include('todo.urls')),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/register/$', register, {'backend': 'registration.backends.simple.SimpleBackend', 'success_url': '/'}, name='registration_register'),
    url(r'^accounts/register/closed/$', direct_to_template, {'template': 'registration/registration_closed.html'}, name='registration_disallowed'),
    url(r'^accounts/', include('registration.auth_urls')),
)
