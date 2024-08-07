from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My courses"
admin.site.index_title = "Welcome to the Courses Shop admin panel"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['created_at'],
                   'classes': ['collapse']}),
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
