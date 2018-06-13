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
        """ Return all the tasks of this user """
        return Task.objects.my_tasks(self.request.user.id)


@login_required(login_url='/tasks/login/')
def my_tasks(request):
    return render(request, 'tasks/my_tasks/index.html', {'tasks': Task.objects.my_tasks(request.user.id)})


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

    return render(request, 'tasks/my_tasks/create.html', {'tasks': Task.objects.from_higher(), 'users': User.objects.all()})

@login_required(login_url='/tasks/login/')
def assign(request):
    return render(request, 'tasks/my_tasks/assign.html', {'users': User.objects.all()})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/tasks')


def login(request):
    if request.method == 'POST':
        if LoginForm(request.POST).is_valid() and authenticate(username=request.POST['username'],
                                                               password=request.POST['password']) is not None:
            auth_login(request, request.POST['username'])
        return HttpResponseRedirect('/tasks')
    return render(request, 'tasks/auth/login.html', {'form': LoginForm()})
