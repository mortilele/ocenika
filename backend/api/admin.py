from django.contrib import admin

from utils import constants
from .models import University, Professor, ProfessorReview, Subject, RatingApplication, PrivacyPolicy


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('university', 'professors')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    exclude = ('full_name',)
    readonly_fields = ('average_rating', 'rating_count')
    list_filter = ('universities', 'subjects')
    search_fields = ('full_name', 'first_name', 'last_name', )


@admin.register(ProfessorReview)
class ProfessorReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'professor', 'status', 'created_at')
    list_filter = ('status', 'professor', 'subject', 'value')
    search_fields = ('review', 'professor__full_name')
    readonly_fields = ('value', )

    def save_model(self, request, obj, form, change):
        if change:
            if 'status' in form.changed_data:
                if obj.status != constants.ON_MODERATION:
                    obj.user.send_review_result(obj)
        super().save_model(request, obj, form, change)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    readonly_fields = ('rating', )
    search_fields = ('name', )


# @admin.register(RatingApplication)
# class RatingApplicationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'is_viewed', 'review')


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', )
