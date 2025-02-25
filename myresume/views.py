from django.shortcuts import HttpResponse, render


def homePage(request):
    return render(request,"index.html")

def portFolio(request):
    return render(request,"portfolio2.html")