from urllib import request
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from test1.forms import StudentForm
from test1.models import Student

# from forms import  StudentForm
# Create your views here
def seeAll(request):
    getAll=Student.objects.all().values()
    if getAll :
        context={
            'list':getAll
        }
        temp=loader.get_template('list.html')

        return HttpResponse(temp.render( context, request))
    else:
        temp=loader.get_template('list.html')
        context={
            'lists':"Dont have Any Student ....."
        }
        return HttpResponse(temp.render(context ,request ))


def add(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('seeAll'))
        else :
            forms=StudentForm()
            return render(request, 'insertEtudiant.html',{'form': forms})
    else :
        forms=StudentForm()
        return render(request, 'insertEtudiant.html', {'form':forms})


def update(request, id):
    # Fetch the student object to update
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        # Bind the form to the POST data and the existing student instance
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # Save the updated student data
            return redirect(reverse('seeAll'))  # Redirect to the list view
    else:
        # Pre-fill the form with the existing student data
        form = StudentForm(instance=student)
    
    # Render the update template with the form
    return render(request, 'insertEtudiant.html', {'form': form})