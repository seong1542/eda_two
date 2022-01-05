from django.shortcuts import render

# Create your views here.
def index(request): #request에 대한 일정한 처리
    return render(request, "index.html",{})