from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', '{{ app_name }}.views.home', name='{{ app_name }}_home'),

                       )
