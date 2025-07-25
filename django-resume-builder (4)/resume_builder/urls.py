from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Personal Information
    path('personal-info/', views.personal_info_view, name='personal_info'),
    
    # Work Experience
    path('work-experience/', views.work_experience_list, name='work_experience_list'),
    path('work-experience/add/', views.work_experience_create, name='work_experience_create'),
    path('work-experience/<int:pk>/edit/', views.work_experience_update, name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', views.work_experience_delete, name='work_experience_delete'),
    
    # Education
    path('education/', views.education_list, name='education_list'),
    path('education/add/', views.education_create, name='education_create'),
    path('education/<int:pk>/edit/', views.education_update, name='education_update'),
    path('education/<int:pk>/delete/', views.education_delete, name='education_delete'),
    
    # Projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # Skills
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_update, name='skill_update'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Certifications
    path('certifications/', views.certification_list, name='certification_list'),
    path('certifications/add/', views.certification_create, name='certification_create'),
    path('certifications/<int:pk>/edit/', views.certification_update, name='certification_update'),
    path('certifications/<int:pk>/delete/', views.certification_delete, name='certification_delete'),
    
    # Awards
    path('awards/', views.award_list, name='award_list'),
    path('awards/add/', views.award_create, name='award_create'),
    path('awards/<int:pk>/edit/', views.award_update, name='award_update'),
    path('awards/<int:pk>/delete/', views.award_delete, name='award_delete'),
    
    # Languages
    path('languages/', views.language_list, name='language_list'),
    path('languages/add/', views.language_create, name='language_create'),
    path('languages/<int:pk>/edit/', views.language_update, name='language_update'),
    path('languages/<int:pk>/delete/', views.language_delete, name='language_delete'),
    
    # Resumes
    path('resumes/', views.resume_list, name='resume_list'),
    path('resumes/create/', views.resume_create, name='resume_create'),
    path('resumes/<int:resume_id>/preview/', views.resume_preview, name='resume_preview'),
    path('resumes/<int:resume_id>/export-pdf/', views.export_pdf, name='export_pdf'),
    path('resumes/<int:resume_id>/export_docx/', views.export_docx, name='export_docx'),
    # Resume Template Selection
    path('resumes/select/', views.resume_template_select, name='resume_template_select'),
    path('resumes/<int:resume_id>/delete/', views.resume_delete, name='resume_delete'),
    
    # References
    path('references/', views.reference_list, name='reference_list'),
    path('references/add/', views.reference_create, name='reference_create'),
    path('references/<int:pk>/edit/', views.reference_update, name='reference_update'),
    path('references/<int:pk>/delete/', views.reference_delete, name='reference_delete'),
    path('resume/classic/preview/', views.resume_classic_preview, name='resume_classic_preview'),
    path('internships/', views.internship_list, name='internship_list'),
    path('internships/add/', views.internship_create, name='internship_create'),
    path('internships/<int:pk>/edit/', views.internship_update, name='internship_update'),
    path('internships/<int:pk>/delete/', views.internship_delete, name='internship_delete'),
]
