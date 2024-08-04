from django.http import HttpResponse


def hello(request, number):
    text = "<h1>welcome to my app number %s!</h1>" % number
    return HttpResponse(text)
