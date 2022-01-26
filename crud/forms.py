from django import forms

from .models import UserData

class UserDataForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = '__all__'  # we can set __all__ because cuser is set to editable=False in model


