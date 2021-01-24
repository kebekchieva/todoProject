from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index2.html")


def test(request):
    return render(request, "test.html")