from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ScriptSpinnerUser
from .forms import ScriptSpinnerUserCreationForm, ScriptSpinnerUserChangeForm, RegisterForm

class ScriptSpinnerUserAdmin(UserAdmin):
    add_form = ScriptSpinnerUserCreationForm
    form = ScriptSpinnerUserChangeForm
    model = ScriptSpinnerUser

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_subscribed',)
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_subscribed',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_subscribed',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 
                'password1', 'password2', 'is_staff', 'is_active',  'is_subscribed',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(ScriptSpinnerUser, ScriptSpinnerUserAdmin)
