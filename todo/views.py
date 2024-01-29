from django.shortcuts import render,redirect
from .models import *

def index(request):
    return render(request,'index.html')

def submit(request):
    obj=Todo()
    obj.title = request.POST.get('title')
    obj.description = request.POST.get('description')
    print(f"Received a {request.method} request")
    obj.save()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)


def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "id" : obj.id,
    }
    return render(request,'edit.html',context=mydictionary)

def update(request, id):
    obj = Todo.objects.get(id=id)
    obj.title = request.GET.get('title')
    obj.description = request.GET.get('description')
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('list')