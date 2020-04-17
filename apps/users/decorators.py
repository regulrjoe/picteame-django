from django.http import HttpResponse
from django.shortcuts import redirect

# ---------------------------------
def unauthenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

# ---------------------------------
def allowed_users(allowed_roles=[]):

    # -----------------------
    def decorator(views_func):

        # -----------------------
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group_is_allowed = False
                for g in request.user.groups_all():
                    if g.name in allowed_roles:
                        group_is_allowed = True
                        break
                if group_is_allowed:
                    return view_func(requst, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorized to view this page.')
            else:
                return HttpResponse('You are not authorized to view this page.')
        # -----------------------

        return wrapper_func
    # -----------------------

    return decorator
