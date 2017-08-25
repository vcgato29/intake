from rest_framework.views import exception_handler
from django.shortcuts import redirect
from rest_framework.exceptions import NotAuthenticated as DRFNotAuthenticated
from django.core.exceptions import ObjectDoesNotExist as DjangoObjectDoesNotExist
from django.core.exceptions import PermissionDenied as DjangoPermissionDenied


def default_django_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    if isinstance(exc, DRFNotAuthenticated):
        raise DjangoPermissionDenied
    else:
        return exception_handler(exc, context)


def redirect_on_permission_denied(*args, **kwargs):
    return redirect('account_login')
