from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Student
from core.forms import StudentForm

# Create your views here.

def index(request):
    form = StudentForm()
    datas = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'core/index.html', {'datas': datas, 'form': form})

def update(request, data_id):
    datas = Student.objects.get(id=data_id)
    form = StudentForm(instance=datas)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=datas)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'core/update.html', {'datas': datas, 'form': form})

def delete(request, data_id):
    if request.method == 'POST':
        Student.objects.get(id=data_id).delete()
        return redirect('index')

