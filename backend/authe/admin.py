from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MainUserChangeForm, MainUserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    # form = MainUserChangeForm
    # add_form = MainUserCreationForm
    list_display = ('id',
                    'email')

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'university',
                'password',
                'transcript',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_active',
                'is_staff',
                'is_confirmed',

            )
        })
    )

    ordering = ('id',)
