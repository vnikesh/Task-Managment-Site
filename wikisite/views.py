from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
from django.http import HttpResponse



# Create your views here.

def home(request):
   return render(request, 'wikisite/home.html',
                 {'wikisite': home})

def login(request):
   return render(request, 'wikisite/login.html',
                 {'wikisite': login})

@login_required
def task_list(request):
    task = Task.objects.filter(Created_Date__lte=timezone.now())
    return render(request, 'wikisite/task_list.html',
                  {'tasks': task})

@login_required
def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.Created_Date = timezone.now()
            # user = User.objects.filter(User_name=request.user.username)[0]
            # print('printing User value ' + str(user))
            # task.User_name = user
            task.save()
            # task = Task.objects.filter(User_name=request.user.username)
            task = Task.objects.filter(Created_Date__lte = timezone.now())
            # print('Print Task' + str(task))
            return render(request, 'wikisite/task_list.html',
                          {'tasks': task})
        # else:
        #     form = TaskForm()
        # return render(request, 'wikisite/task_new.html', {'form': form})

    else:
        form = TaskForm()
    return render(request, 'wikisite/task_new.html', {'form': form})




@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.updated_date = timezone.now()
            task.save()
            task = Task.objects.filter(Created_Date__lte=timezone.now())
            return render(request, 'wikisite/task_list.html',
                          {'tasks': task})
    else:
        form = TaskForm(instance=task)
    return render(request, 'wikisite/task_edit.html', {'form': form})



@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('wikisite:task_list')


@login_required
def summary(request):
    # task = get_object_or_404(Task, pk=pk)
    tasks = Task.objects.filter(Created_Date__lte=timezone.now())

    return render(request, 'wikisite/summary.html', {'tasks': tasks})




