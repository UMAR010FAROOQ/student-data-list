from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentForm
from .models import User
# Create your views here.
def student(request):
    if request.method == 'POST':
        studentData = StudentForm(request.POST)
        if studentData.is_valid():
            nm = studentData.cleaned_data['name']
            em = studentData.cleaned_data['email']
            pw = studentData.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            studentData = StudentForm() 
    else:
        studentData = StudentForm()    
    
    stud = User.objects.all()
    
    return render(request, 'student.html', {'form': studentData, 'stud':stud})


def update_data(request, id):
    if request.method == "POST":
        studentData = User.objects.get(pk=id)
        updateData = StudentForm(request.POST, instance=studentData)
        if updateData.is_valid():
            updateData.save()
            return redirect('student')  
    else:
        studentData = User.objects.get(pk=id)
        updateData = StudentForm(request.POST, instance=studentData)
           
    return render(request, 'updateStudent.html', {'updateData':updateData})

def delete_data(request, id):
    if request.method == 'POST':
        delete_item = User.objects.get(pk=id)
        delete_item.delete()
        return HttpResponseRedirect('/')