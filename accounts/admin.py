from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'is_active', 'date_joined')
    list_display_links = ('email', 'first_name', 'last_name') # options opens the edit detail page of user 
    readonly_fields = ( 'last_login', 'date_joined') # make the field non-editable from admin page edit form 
    ordering = ('-date_joined',) # - => descending order ,sort order

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 


admin.site.register(Account,AccountAdmin)