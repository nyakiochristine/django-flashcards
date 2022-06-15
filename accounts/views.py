from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def dashboardViews(request):
    return render(request,'dashboard.html')

def registerViews(request):
    return render(request,'registration/register.html')