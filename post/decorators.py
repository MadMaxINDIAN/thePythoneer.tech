from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticted_user_only(view_func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect("/")
        return view_func(req, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(req, *args, **kwargs):
            group = []
            for o in req.user.groups.all():
                group.append(o.name)
            if any(item in group for item in allowed_roles):
                return view_func(req, *args, **kwargs)
            return HttpResponse("You are not authorised")
        return wrapper_func
    return decorator