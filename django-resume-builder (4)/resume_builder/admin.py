from django.contrib import admin
from .models import *

@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'city', 'state']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['city', 'state', 'country']

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'start_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['position', 'company', 'location']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['degree', 'institution', 'field_of_study']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'start_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['title', 'technologies']

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'category']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'expiry_date']
    list_filter = ['issue_date', 'expiry_date']
    search_fields = ['name', 'issuing_organization']

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuing_organization', 'date_received']
    list_filter = ['date_received']
    search_fields = ['title', 'issuing_organization']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency']
    list_filter = ['proficiency']
    search_fields = ['name']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'template', 'is_active', 'created_at']
    list_filter = ['template', 'is_active', 'created_at']
    search_fields = ['title', 'user__username']
