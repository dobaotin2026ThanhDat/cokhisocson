from django.shortcuts import render


def home(request):

    return render(request,"home/home.html")


def about(request):

    return render(request,"pages/about.html")


def profile(request):

    return render(request,"pages/profile.html")


def quote(request):

    return render(request,"pages/quote.html")


def services(request):

    return render(request,"services/services.html")


def projects(request):

    return render(request,"projects/projects.html")