from django.contrib import admin
from students.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'nid', 'phone']


admin.site.register(User, UserAdmin)
