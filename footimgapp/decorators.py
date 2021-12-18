from django.http import HttpResponseForbidden
from footimgapp.models import Footimg


def footimg_ownership_required(func):
    def decorated(request, *args, **kwargs):
        footimg = Footimg.objects.get(pk=kwargs['pk'])
        if not footimg.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated