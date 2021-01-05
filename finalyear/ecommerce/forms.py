from django import forms
from ecommerce.models import register

class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = "__all__"
