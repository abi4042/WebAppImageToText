# Abhilasha has created this fle

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def remove_punctuation(request):
    return HttpResponse('''remove punc  <a href="/"> back </a> ''')


def capitalize_first(request):
    return HttpResponse("captitalize_first")


def newline_remover(request):
    return HttpResponse("newline_remover")

