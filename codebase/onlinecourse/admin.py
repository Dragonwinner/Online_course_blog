from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 10
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time', 'total_learners']
    list_display = ['user', 'full_time', 'total_learners']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor , InstructorAdmin)
admin.site.register(Learner)
