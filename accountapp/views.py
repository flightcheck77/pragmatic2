from django.shortcuts import render
# from django.http import HttpResponse


# def hello_world(request):
#     return HttpResponse('Initial setup for flightcheck77/pragmatic2')


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')