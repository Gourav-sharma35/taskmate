from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models  import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            a=form.save(commit=False)
            a.manager=request.user
            a.save()
        messages.success(request,("New Task added"))
        return redirect("todolist")
    else:
        all_task=TaskList.objects.filter(manager = request.user)
        paginator=Paginator(all_task,10)
        page=request.GET.get('pg')
        all_task=paginator.get_page(page)

        return render(request,'todolist.html',{'all_task':all_task})

@login_required
def index(request):
    context={"index_text":"Welcome Home Page"}
    return render(request,'index.html',context)


@login_required
def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.delete()
    else:
        messages.error(request,("Accessed Restricted! You cannot permission to accessed this.."))

    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method=="POST":
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task is edited"))
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

@login_required
def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Accessed restricted! You cannot permission to accessed this.."))    
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')



def contact(request):
    context={"contact_text":"hi this is contact us page"}
    return render(request,'contact.html',context)

def about(request):
    context={"about_text":"hi this is a about page"}
    return render(request,'about.html',context)
