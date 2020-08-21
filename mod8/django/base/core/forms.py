from core.models import Student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

class UserCreationForm(UserCreationForm):
    model = User
    fields = '__all__'


