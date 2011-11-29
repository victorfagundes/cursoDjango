# Create your views here.
from django.shortcuts import render

def produtos(request):
    return render(request, "produtos.html", locals())
