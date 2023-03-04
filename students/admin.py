from django.contrib import admin
from students.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'nid', 'phone']
    list_filter = ['name', 'address', 'nid', 'phone']
    search_fields = ['name', 'address', 'nid', 'phone']
    list_per_page = 10


admin.site.register(User, UserAdmin)
