from django.shortcuts import render,redirect, get_object_or_404,reverse
from sqlalchemy import true

import to_do_app
from .models import ToDo
from django.contrib.auth.decorators import login_required
from .forms import ToDoForm
from django.contrib import messages
# Create your views here.


@login_required(login_url='user:login')
def index(request):
    todos = ToDo.objects.filter(user = request.user)
    context = {
        "todos" :todos,
    }
    return render (request, "index.html", context)

@login_required(login_url='user:login')
def done(request,id):
    todo = ToDo.objects.filter(id = id).first()
    todo.status = not True
    todo.save()
    return redirect('to_do_app:index')


@login_required(login_url='user:login')
def detail(request,id):
    todo = ToDo.objects.filter(id = id).first()
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html',context)
    
@login_required(login_url='user:login')
def edit(request, id):
    todo = get_object_or_404(ToDo, id=id)
    form = ToDoForm(request.POST or None,  instance = todo )
    # initial = {'finishdate': todo.finishdate}
    # form = ToDoForm(initial=initial)

 
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.finishdate = request.POST.get('finishdate')
        todo.save()
        messages.success(request, "Task Redaktə Edildi")
        return redirect(reverse('to_do_app:detail', kwargs={'id':id}))
    context={
        "form":form,
    }
    return render(request, 'edit.html', context)

@login_required(login_url='user:login')
def add_task(request):
    form = ToDoForm(request.POST or None)
    context={
        "form":form,
    }



    if form.is_valid():
        todo = form.save(commit = False)
        todo.finishdate = request.POST.get('finishdate')
        todo.user = request.user
        todo.save()
        
        messages.success(request, "Task Əlavə Edildi")

    return render(request, "add_task.html", context)
def  delete(request,id):
    todo = get_object_or_404(ToDo, id = id)
    todo.delete()
    return redirect('to_do_app:index')
