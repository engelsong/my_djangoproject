from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>The HomePage</h1>")
    return render(request, 'page/page.html')

# Create your views here.
