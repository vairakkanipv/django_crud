from django.shortcuts import render, redirect
from crud_operations.forms import EmployeeForm
from crud_operations.models import Employee

# Create your views here.
def index(request):
    all_emp = Employee.objects.all()
    return render(request,'index.html',{'data':all_emp})

def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request,'create.html',context)

def update(request, id):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('index')
        return redirect('update')
    else:
        form = EmployeeForm
    context = {
        'form': form
    }
    return render(request,'update.html',context)

def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('index')
    #return render(request,'delete.html')
