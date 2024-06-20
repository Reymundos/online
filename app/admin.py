from django.contrib import admin
from .models import Course, CourseThema, LikeDislike, Comment, News, Video

# Register your models here.


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


@admin.register(CourseThema)
class CourseThemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    list_display_links = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course_thema', 'autor', 'created')
    list_display_links = ('course_thema',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_display_links = ('title',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('course', 'course_thema', 'video')
    list_display_links = ('course', )
    list_editable = ('course_thema',)
