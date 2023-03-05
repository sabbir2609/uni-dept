from django.contrib import admin
from students.models import User, Course


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'nid', 'phone']
    list_filter = ['name', 'address', 'nid', 'phone']
    search_fields = ['name', 'address', 'nid', 'phone']
    list_per_page = 10


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description']
    list_filter = ['name', 'code', 'description']
    search_fields = ['name', 'code', 'description']
    list_per_page = 10


admin.site.register(Course, CourseAdmin)
admin.site.register(User, UserAdmin)
