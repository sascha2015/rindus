from cuser.middleware import CuserMiddleware
from django import forms

from .models import UserData

class UserDataForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = '__all__'  # we can set __all__ because cuser is set to editable=False in model

    # When saving data we have to add auth.User to UserData.cuser
    # clean() has no access to request to get the current user
    # get user object from CuserMiddleware
    # test if UserData.cuser is empty (in case if new record or admin who created the userdata has been deleted
    # (Note: UserData.cuser on_delete is set to SET_NULL to avoid deleting a user only because of deleting the admin)
    def clean (self):

        if not self.instance.cuser:
            self.instance.cuser = CuserMiddleware.get_user()

