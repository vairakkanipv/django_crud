from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    return render(request,'create.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')
