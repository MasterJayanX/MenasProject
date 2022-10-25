from django import forms
from .models import Login


#recordar usar el makemirations y el migrate
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        exclude = ["fecha"]