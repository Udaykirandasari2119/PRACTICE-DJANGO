from django import forms
from DbApp.models import Employee
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def validateAge(p_age):
    if p_age<30:
        raise ValidationError('Age should not be less than 30')
    
class FirstForm(forms.Form):
    name = forms.CharField(max_length=20,required=False,
                           widget=forms.TextInput(attrs={'style':{'height':'4px'}}))
    age = forms.IntegerField(validators=[validateAge])
    doj = forms.DateField(widget=forms.SelectDateWidget)

    def clean_name(self):
        p_name = self.cleaned_data['name']
        if p_name.startswith('s') == False:
            raise ValidationError('Name is not starting with s')
        return p_name
    
    """def clean_age(self):
        p_age = self.cleaned_data['age']
        if p_age<30:
            raise ValidationError('age should not be less than 30')
        return p_age"""
    
class EmpForm(forms.Form):
    empno = forms.IntegerField()
    empname = forms.CharField(max_length=20)
    salary = forms.IntegerField()
    department = forms.IntegerField()

class EmpmodelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1','email','password2','is_superuser']