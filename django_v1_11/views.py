
from django.shortcuts import get_object_or_404, render


def index(request):
    context = {'message': 'hello there'}
    return context