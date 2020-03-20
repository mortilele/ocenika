from django.contrib import admin
from .models import University, Professor, ProfessorRating, Subject


# Register your models here.
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    exclude = ('full_name',)


@admin.register(ProfessorRating)
class ProfessorRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'professor', 'created_at')


class SubjectAdmin(admin.TabularInline):
    model = Subject


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    inlines = [SubjectAdmin]
