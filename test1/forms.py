from django import forms

from test1.models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['nom' , 'email']























