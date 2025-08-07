from django.shortcuts import render, HttpResponse
def tutorsHome(request):
    return render(request, "home.html")