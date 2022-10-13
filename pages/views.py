from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hellow, World!")