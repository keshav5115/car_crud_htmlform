from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Car
# Create your views here.

def Carview(request):
    print('method:-', request.method)
    if request.method =='POST':
        cname=request.POST.get('cname')
        model=request.POST['model']
        price=request.POST['price']
        variant=request.POST['variant']
        color=request.POST.get('color')
        engine=request.POST['engine']
        Car.objects.create(cname=cname,model=model,price=price,variant=variant,color=color,engine=engine)
        return redirect('/form/readall/')
    return render(request,'cartemp.html')


def readview(request):
    obj=Car.objects.all()
    
    return render(request,'readcar.html',{'obj':obj})


def read(request):
    obj=Car.objects.all()
    if request.method=='POST':
        pk=request.POST['cars']
        obj=Car.objects.get(cname=pk)
        return render(request,'readone.html',{'obj':obj})

    return render(request,'read.html',{'obj':obj})



def readone(request,pk):
    obj=Car.objects.get(id=pk)
    return render(request,'readone.html',{'obj':obj})


def updateone(request,pk):
    obj=Car.objects.get(id=pk)

    if request.method=='POST':
        cname=request.POST.get('cname')
        model=request.POST['model']
        price=request.POST['price']
        variant=request.POST['variant']
        color=request.POST.get('color')
        engine=request.POST['engine']
        obj=Car.objects.filter(id=pk).update(cname=cname,model=model,price=price,variant=variant,color=color,engine=engine)
        return redirect('/form/readall/')
    return render(request,'updateone.html',{'obj':obj})

def updateread(request):
    obj=Car.objects.all()
    if request.method=='POST':
        print(request.POST['cars'])
        obj=Car.objects.get(cname=request.POST['cars'])
        return render(request,'updateone.html',{'obj':obj})
    return render(request,'updateread.html',{'obj':obj})


def delete(request,pk):
    obj=Car.objects.get(id=pk).delete()
    return redirect('/form/readall/')







def sample(request):
    return HttpResponse('data is submited')