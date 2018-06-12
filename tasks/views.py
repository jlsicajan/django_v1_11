from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Task


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# GENERIC VIEWS

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    login_url = '/tasks/login/'

    def get_queryset(self):
        """ Return all the tasks """
        return Task.objects.filter(created_by=self.request.user.id).order_by('-priority')


@login_required(login_url='/tasks/login/')
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user.id).order_by('-priority')
    return render(request, 'tasks/my_tasks/index.html', {'tasks': tasks})


@login_required(login_url='/tasks/delete/')
def delete_task(request):
    tasks = Task.objects.order_by('priority')
    return render(request, 'tasks/my_tasks/create.html', {'tasks': tasks})


@login_required(login_url='/tasks/login/')
def create_task(request):
    if request.method == 'POST':
        # for key in request.POST:
        #     print(key)
        #     value = request.POST[key]
        #     print(value)
        task_name = request.POST['task_name']
        priority = request.POST['priority']

        new_task = Task()
        new_task.name = task_name
        new_task.TASK_PRIORITY = priority
        new_task.created_by = request.user
        new_task.assigned_to = request.user

        new_task.save()
    tasks = Task.objects.order_by('priority')
    return render(request, 'tasks/my_tasks/create.html', {'tasks': tasks})


@login_required(login_url='/tasks/login/')
def assign(request):
    if request.method == 'POST':
        print('hello there')
        
    return render(request, 'tasks/my_tasks/assign.html', {'users': User.objects.all()})


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
