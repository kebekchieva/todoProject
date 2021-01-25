from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index2.html")


def test(request):
    return render(request, "test.html")

    def test(request):
        todo_list = ToDo.object.all()
        return render (request, "test.html", {"todo_list": todo_list})