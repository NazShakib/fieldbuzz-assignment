from django.shortcuts import redirect
from . cookie import getCookie


### user is authenticated
def is_authenticated(view_fun):
    def wapper_fun(request, *args, **kwargs):
        if getCookie(request,'token') is not None:
            return redirect('home')
        else:
            return view_fun(request,*args, **kwargs)
    return wapper_fun

### user is unauthenticated
def unAthenticated(view_fun):
    def wapper_fun(request, *args, **kwargs):
        if getCookie(request,'token') is not None:
            return view_fun(request,*args, **kwargs)
        else:
            return redirect('/')
    return wapper_fun