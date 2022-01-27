from cuser.middleware import CuserMiddleware
from django.contrib import admin

from .models import UserData
from .forms import UserDataForm

admin.site.site_header = 'Rindus User Administration'

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    form = UserDataForm

    # on list view display username and administrator who created them
    list_display = ("first_name", "last_name", "cuser")

    # hook into amdin function to check user change permission
    # test if current user is creater of user data
    # if false, deny change permission
    # this way the admin doesn't have an option to change field value (only readable) and no "save" button
    # this is much more userfriendly than first let the user change data and later deny saving
    def has_change_permission(self, request, obj=None):

        if obj and obj.cuser:

            user = CuserMiddleware.get_user()

            if user and obj.cuser != user:
                return False

        return super(UserDataAdmin, self).has_change_permission(request, obj)

    # hook into amdin function to check user delete permission
    # if false, deny delete permission by removing delete button
    def has_delete_permission(self, request, obj=None):

        user = CuserMiddleware.get_user()

        if not UserData.objects.filter(cuser=user):
            return False

        if obj and obj.cuser:

            user = CuserMiddleware.get_user()

            if user and obj.cuser != user:
                return False

        return super(UserDataAdmin, self).has_delete_permission(request, obj)

    # this function is used by admin to show objects which can be deleted after marking records in list view and
    # delete is clicked
    # overwrite and test if user has permission to delete objects
    def get_deleted_objects(self, objs, request):

        user = CuserMiddleware.get_user()
        delete_objects = []
        protected_objects = []
        object_counts = {}
        perms_needed = set()
        count = 0

        for o in objs:

            if o.cuser == user:
                delete_objects.append (f'User Data: {o.__str__()}')
                object_counts.update ({count : o.__str__()})
                count += 1

            else:
                protected_objects.append (o.id)
                perms_needed.add (f'User Data: {o.__str__()}')

        return delete_objects, { "User Data" : count}, perms_needed, protected_objects
