from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_staff', 'is_active', 'date_joined') 
    list_filter = ('is_staff', 'is_active')  
    search_fields = ('name',)  
    ordering = ('name',)  