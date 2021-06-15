from django.shortcuts import render
from crud_operations.forms import EmployeeForm

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

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')
