from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People


# Create your views here.
def demo(request):
    print(request)
    obj=Place.objects.all()
    obj1 = People.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
def demo1(request):
    obj1=People.objects.all()
    return render(request,"index.html",{'result1':obj1})



# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
