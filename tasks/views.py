from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.db.models import ProtectedError
import json

from .forms import LoginForm
from .models import Task

# GENERIC VIEWS
class IndexView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    login_url = '/tasks/login/'

    def get_queryset(self):
        """ Return all the tasks of this user """
        return Task.objects.my_tasks(self.request.user.id)

# LIST VIEW
# class TaskListView(LoginRequiredMixin, ListView):
#     model = Task


@login_required(login_url='/tasks/login/')
def my_tasks(request):
    return render(request, 'tasks/my_tasks/index.html', {'tasks': Task.objects.assigned_to_me(request.user.id)})


@login_required(login_url='/tasks/delete/')
def delete_task(request):
    return render(request, 'tasks/my_tasks/create.html', {'tasks': Task.objects.from_lower()})


@login_required(login_url='/tasks/login/')
def create_task(request):

    if request.method == 'POST':
        new_task = Task()
        new_task.name = request.POST['task_name']
        new_task.priority = request.POST['priority']
        new_task.assigned_to = User.objects.get(pk=request.POST['assigned_to'])
        new_task.created_by = request.user
        new_task.save()
        return HttpResponseRedirect('/tasks/create')

    tasks_json = {}
    for task_info in Task.objects.all():
        tasks_json[task_info.id] = [task_info.name, task_info.priority, task_info.assigned_to.first_name]

    return render(request, 'tasks/my_tasks/create.html', {
        'tasks': Task.objects.from_higher(), 'users': User.objects.all(),
        'tasks_json': json.dumps(tasks_json)})


@login_required(login_url='/tasks/login/')
def assign(request):
    return render(request, 'tasks/my_tasks/assign.html', {'users': User.objects.all()})

@login_required(login_url='/tasks/login/')
def delete_task(request):
    task_id = request.POST.get('task_id', None)

    try:
        Task.objects.filter(id=task_id).delete()
    except ProtectedError:
        return HttpResponse(False)

    return HttpResponse(True)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/tasks')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print('============ CHECKING FOR ==========')
            print('Username: ' + username)
            print('Password: ' + password)

        user = authenticate(username=username, password=password)
        print('=========== USER AUTHENTICATE ==============')
        print(user)
        if user is not None:
            auth_login(request, user)

        return HttpResponseRedirect('/tasks')

    else:
        form = LoginForm()

    return render(request, 'tasks/auth/login.html', {'form': form})
