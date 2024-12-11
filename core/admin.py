from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Requirement
from django import forms
from django.utils.translation import gettext_lazy as _

# Custom User Admin Form to display the extra fields in the User model
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'name', 'surname', 'phone_number', 'profile_picture', 'is_active', 'is_supended')

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'name', 'surname', 'phone_number', 'profile_picture')

# Custom User Admin to use the custom forms and to display user info effectively
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # Customize list display
    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'is_active', 'is_supended')
    list_filter = ('role', 'is_active', 'is_supended')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    # Add additional fields in the user creation and change forms
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'name', 'surname', 'phone_number', 'profile_picture')}),
        (_('Permissions'), {'fields': ('role', 'is_active', 'is_supended', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'name', 'surname', 'phone_number', 'profile_picture')}),
        (_('Permissions'), {'fields': ('role', 'is_active', 'is_supended')}),
    )
    filter_horizontal = ('groups', 'user_permissions')

# Register CustomUser with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Custom Requirement Admin
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'priority', 'status', 'feature', 'version')
    list_filter = ('priority', 'status', 'created_at')
    search_fields = ('title', 'description', 'feature')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'version', 'previous_version')

    # Make 'attachments' field editable inline
    fieldsets = (
        (None, {'fields': ('title', 'description', 'created_by', 'priority', 'status', 'feature')}),
        (_('Attachments'), {'fields': ('attachments',)}),
        (_('Version Control'), {'fields': ('version', 'previous_version')}),
    )

# Register Requirement model with custom admin view
admin.site.register(Requirement, RequirementAdmin)
