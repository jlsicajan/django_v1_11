
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, '', {
        'question': 'hello',
        'error_message': "You didn't select a choice.",
    })