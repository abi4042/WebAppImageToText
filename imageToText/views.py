# Abhilasha has created this fle
import string
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    ## Get the text
    text_to_remove = request.GET.get("text", 'default')
    remove_punc = request.GET.get("remove_punc", 'off')

    # Analyze the text
    punctuations = string.punctuation
    analysed_text = ""
    for char in text_to_remove:
        if char not in punctuations:
            analysed_text += char

    params = {'analyzing_text': analysed_text, 'purpose': "remove punctuation"}
    return render(request, 'analyze.html', params)

#
# def capitalize_first(request):
#     return HttpResponse("captitalize_first")
#
#
# def newline_remover(request):
#     return HttpResponse("newline_remover")

