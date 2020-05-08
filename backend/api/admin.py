from django.contrib import admin
from .models import University, Professor, ProfessorReview, Subject, RatingApplication


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    exclude = ('full_name',)
    readonly_fields = ('average_rating', 'rating_count')


@admin.register(ProfessorReview)
class ProfessorReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'professor', 'created_at')


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(RatingApplication)
class RatingApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_viewed', 'review')
