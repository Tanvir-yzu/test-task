from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the tasks app!")

def manager_dashboard(request):
    return render(request, 'admin-dashboard.html')
def user_dashboard(request):
    return render(request, 'user-dashboard.html')
