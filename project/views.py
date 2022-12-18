from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.shortcuts import render
from django.shortcuts import redirect
from .models import ProductModel
from .forms import Product

# Create your views here.
def index(request):
    return render(request, 'project/index.html')

def create(request):
    context = {}
    form = Product(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('project:view')
    context['form'] = form
    return render(request, 'project/create.html', context)

def view(request):
    context = {}
    context["dataset"] = ProductModel.objects.all()
    return render(request, 'project/view.html', context)

def detail(request, id):
    context ={}
    context["data"] = ProductModel.objects.get(id = id)
    return render(request, 'project/detail.html', context)

from django.urls import path
from .views import detail

urlpatterns = [
    path('<id>', detail, name='detail'),
]

def update(request, id):
    context ={}
    object = get_object_or_404(ProductModel, id = id)
    form = Product(request.POST or None, instance = object)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/project/view/'+id)
    context["form"] = form
    return render(request, "project/update.html", context)

def delete(request, id):
    context ={}
    object = get_object_or_404(ProductModel, id = id)
    if request.method =="POST":
        object.delete()
        return HttpResponseRedirect("/project/view")
    return render(request, "project/delete.html", context)