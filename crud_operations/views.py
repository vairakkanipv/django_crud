from django.shortcuts import render
from crud_operations.forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request,'create.html',context)

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')
