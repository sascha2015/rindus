from django.contrib import admin

from .models import UserData
from .forms import UserDataForm

admin.site.site_header = 'Rindus User Administration'

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    form = UserDataForm

    # on list view display username and administrator who created them
    list_display = ("first_name", "last_name", "cuser")
