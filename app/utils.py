from django.shortcuts import redirect


def session_required(view_func):
    def wrapper(request, *args, **kwargs):
        if "dpilogin" not in request.session:
            return redirect("inicio")
        return view_func(request, *args, **kwargs)
    return wrapper

