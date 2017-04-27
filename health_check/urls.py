from django.conf.urls import url
from django.http import HttpResponse


def ok(request, *args, **kwargs):
    return HttpResponse(status=200)


def error(request, *args, **kwargs):
    return HttpResponse(status=500)


urlpatterns = [
    url(r'^$', ok, name='health_check-ok'),
    url(r'^error$', error, name='health_check-error'),
]
