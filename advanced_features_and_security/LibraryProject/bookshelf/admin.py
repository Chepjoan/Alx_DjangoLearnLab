from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

<<<<<<< HEAD
=======

>>>>>>> 5e4bc08a88140142f400fd0f79ecfd19e4c29f3a
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

<<<<<<< HEAD
=======

>>>>>>> 5e4bc08a88140142f400fd0f79ecfd19e4c29f3a
admin.site.register(CustomUser, CustomUserAdmin)
