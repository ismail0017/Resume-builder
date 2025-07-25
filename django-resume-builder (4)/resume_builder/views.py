from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from .models import *
from .forms import *
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from django.urls import reverse
from wkhtmltopdf.views import PDFTemplateResponse
# from weasyprint import HTML  # Disabled to allow server to start

def require_resume(request):
    if not Resume.objects.filter(user=request.user).exists():
        messages.warning(request, 'You must create a resume before adding other information.')
        return redirect('resume_template_select')
    return None

@login_required
def dashboard(request):
    context = {
        'personal_info': PersonalInfo.objects.filter(user=request.user).first(),
        'work_experiences': WorkExperience.objects.filter(user=request.user).order_by('-start_date')[:3],
        'educations': Education.objects.filter(user=request.user).order_by('-start_date')[:2],
        'projects': Project.objects.filter(user=request.user).order_by('-start_date')[:3],
        'skills': TechnicalSkill.objects.filter(user=request.user)[:5],
        'certifications': Certification.objects.filter(user=request.user).order_by('-issue_date')[:3],
        'awards': Award.objects.filter(user=request.user).order_by('-date_received')[:3],
        'languages': Language.objects.filter(user=request.user)[:3],
        'resumes': Resume.objects.filter(user=request.user),
    }
    return render(request, 'resume_builder/dashboard.html', context)

@login_required
def personal_info_view(request):
    personal_info, created = PersonalInfo.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=personal_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal information updated successfully!')
            return redirect('personal_info')
    else:
        form = PersonalInfoForm(instance=personal_info)
    
    return render(request, 'resume_builder/personal_info.html', {'form': form})

@login_required
def work_experience_list(request):
    check = require_resume(request)
    if check: return check
    work_experiences = WorkExperience.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'resume_builder/work_experience_list.html', {'work_experiences': work_experiences})

@login_required
def work_experience_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            messages.success(request, 'Work experience added successfully!')
            return redirect('work_experience_list')
    else:
        form = WorkExperienceForm()
    
    return render(request, 'resume_builder/work_experience_form.html', {'form': form, 'title': 'Add Work Experience'})

@login_required
def work_experience_update(request, pk):
    experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Work experience updated successfully!')
            return redirect('work_experience_list')
    else:
        form = WorkExperienceForm(instance=experience)
    
    return render(request, 'resume_builder/work_experience_form.html', {'form': form, 'title': 'Edit Work Experience'})

@login_required
def work_experience_delete(request, pk):
    experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Work experience deleted successfully!')
        return redirect('work_experience_list')
    
    return render(request, 'resume_builder/work_experience_confirm_delete.html', {'experience': experience})

@login_required
def education_list(request):
    check = require_resume(request)
    if check: return check
    educations = Education.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'resume_builder/education_list.html', {'educations': educations})

@login_required
def education_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            messages.success(request, 'Education added successfully!')
            return redirect('education_list')
    else:
        form = EducationForm()
    
    return render(request, 'resume_builder/education_form.html', {'form': form, 'title': 'Add Education'})

@login_required
def education_update(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education updated successfully!')
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)
    
    return render(request, 'resume_builder/education_form.html', {'form': form, 'title': 'Edit Education'})

@login_required
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education deleted successfully!')
        return redirect('education_list')
    
    return render(request, 'resume_builder/education_confirm_delete.html', {'education': education})

@login_required
def project_list(request):
    check = require_resume(request)
    if check: return check
    projects = Project.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'resume_builder/project_list.html', {'projects': projects})

@login_required
def project_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    return render(request, 'resume_builder/project_form.html', {'form': form, 'title': 'Add Project'})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'resume_builder/project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    
    return render(request, 'resume_builder/project_confirm_delete.html', {'project': project})

@login_required
def skill_list(request):
    check = require_resume(request)
    if check: return check
    skills = TechnicalSkill.objects.filter(user=request.user).order_by('category', 'name')
    return render(request, 'resume_builder/skill_list.html', {'skills': skills})

@login_required
def skill_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = TechnicalSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('skill_list')
    else:
        form = TechnicalSkillForm()
    
    return render(request, 'resume_builder/skill_form.html', {'form': form, 'title': 'Add Skill'})

@login_required
def skill_update(request, pk):
    skill = get_object_or_404(TechnicalSkill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TechnicalSkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('skill_list')
    else:
        form = TechnicalSkillForm(instance=skill)
    
    return render(request, 'resume_builder/skill_form.html', {'form': form, 'title': 'Edit Skill'})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(TechnicalSkill, pk=pk, user=request.user)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('skill_list')
    
    return render(request, 'resume_builder/skill_confirm_delete.html', {'skill': skill})

@login_required
def certification_list(request):
    check = require_resume(request)
    if check: return check
    certifications = Certification.objects.filter(user=request.user).order_by('-issue_date')
    return render(request, 'resume_builder/certification_list.html', {'certifications': certifications})

@login_required
def certification_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user
            certification.save()
            messages.success(request, 'Certification added successfully!')
            return redirect('certification_list')
    else:
        form = CertificationForm()
    
    return render(request, 'resume_builder/certification_form.html', {'form': form, 'title': 'Add Certification'})

@login_required
def certification_update(request, pk):
    certification = get_object_or_404(Certification, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            messages.success(request, 'Certification updated successfully!')
            return redirect('certification_list')
    else:
        form = CertificationForm(instance=certification)
    
    return render(request, 'resume_builder/certification_form.html', {'form': form, 'title': 'Edit Certification'})

@login_required
def certification_delete(request, pk):
    certification = get_object_or_404(Certification, pk=pk, user=request.user)
    if request.method == 'POST':
        certification.delete()
        messages.success(request, 'Certification deleted successfully!')
        return redirect('certification_list')
    
    return render(request, 'resume_builder/certification_confirm_delete.html', {'certification': certification})

@login_required
def award_list(request):
    check = require_resume(request)
    if check: return check
    awards = Award.objects.filter(user=request.user).order_by('-date_received')
    return render(request, 'resume_builder/award_list.html', {'awards': awards})

@login_required
def award_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = AwardForm(request.POST)
        if form.is_valid():
            award = form.save(commit=False)
            award.user = request.user
            award.save()
            messages.success(request, 'Award added successfully!')
            return redirect('award_list')
    else:
        form = AwardForm()
    
    return render(request, 'resume_builder/award_form.html', {'form': form, 'title': 'Add Award'})

@login_required
def award_update(request, pk):
    award = get_object_or_404(Award, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AwardForm(request.POST, instance=award)
        if form.is_valid():
            form.save()
            messages.success(request, 'Award updated successfully!')
            return redirect('award_list')
    else:
        form = AwardForm(instance=award)
    
    return render(request, 'resume_builder/award_form.html', {'form': form, 'title': 'Edit Award'})

@login_required
def award_delete(request, pk):
    award = get_object_or_404(Award, pk=pk, user=request.user)
    if request.method == 'POST':
        award.delete()
        messages.success(request, 'Award deleted successfully!')
        return redirect('award_list')
    
    return render(request, 'resume_builder/award_confirm_delete.html', {'award': award})

@login_required
def language_list(request):
    check = require_resume(request)
    if check: return check
    languages = Language.objects.filter(user=request.user).order_by('name')
    return render(request, 'resume_builder/language_list.html', {'languages': languages})

@login_required
def language_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.user = request.user
            language.save()
            messages.success(request, 'Language added successfully!')
            return redirect('language_list')
    else:
        form = LanguageForm()
    
    return render(request, 'resume_builder/language_form.html', {'form': form, 'title': 'Add Language'})

@login_required
def language_update(request, pk):
    language = get_object_or_404(Language, pk=pk, user=request.user)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            messages.success(request, 'Language updated successfully!')
            return redirect('language_list')
    else:
        form = LanguageForm(instance=language)
    
    return render(request, 'resume_builder/language_form.html', {'form': form, 'title': 'Edit Language'})

@login_required
def language_delete(request, pk):
    language = get_object_or_404(Language, pk=pk, user=request.user)
    if request.method == 'POST':
        language.delete()
        messages.success(request, 'Language deleted successfully!')
        return redirect('language_list')
    
    return render(request, 'resume_builder/language_confirm_delete.html', {'language': language})

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'resume_builder/resume_list.html', {'resumes': resumes})

@login_required
def resume_template_select(request):
    templates = ResumeTemplate.objects.filter(is_active=True)
    return render(request, 'resume_builder/resume_template_select.html', {'templates': templates})

@login_required
def resume_create(request):
    selected_template_id = request.session.get('selected_template_id')
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            if selected_template_id:
                resume.template_id = selected_template_id
            resume.save()
            messages.success(request, 'Resume created successfully!')
            # Optionally clear the session after use
            if 'selected_template_id' in request.session:
                del request.session['selected_template_id']
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resume_builder/resume_form.html', {'form': form, 'title': 'Create Resume'})

@login_required
def resume_preview(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
    
    context = {
        'resume': resume,
        'personal_info': PersonalInfo.objects.filter(user=request.user).first(),
        'work_experiences': WorkExperience.objects.filter(user=request.user).order_by('-start_date'),
        'educations': Education.objects.filter(user=request.user).order_by('-start_date'),
        'projects': Project.objects.filter(user=request.user).order_by('-start_date'),
        'technical_skills': TechnicalSkill.objects.filter(user=request.user).order_by('category', 'name'),
        'certifications': Certification.objects.filter(user=request.user).order_by('-issue_date'),
        'awards': Award.objects.filter(user=request.user).order_by('-date_received'),
        'languages': Language.objects.filter(user=request.user).order_by('name'),
        'internships': Internship.objects.filter(user=request.user).order_by('-start_date'),
        'references': Reference.objects.filter(user=request.user),
    }
    
    template_name = getattr(resume.template, 'name', '').lower() if hasattr(resume, 'template') else ''
    if template_name == 'yellow modern':
        return render(request, 'resume_builder/resume_template_modern_yellow.html', context)
    elif template_name == 'professional':
        return render(request, 'resume_builder/resume_template_professional.html', context)
    elif template_name == 'classic':
        return render(request, 'resume_builder/resume_template_classic.html', context)
    elif template_name == 'modern':
        return render(request, 'resume_builder/resume_template_modern_sidebar.html', context)
    elif template_name == 'minimalist':
        return render(request, 'resume_builder/resume_template_minimalist.html', context)
    return render(request, 'resume_builder/resume_preview.html', context)

@login_required
def export_pdf(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
    # Gather user data
    personal_info = PersonalInfo.objects.filter(user=request.user).first()
    work_experiences = WorkExperience.objects.filter(user=request.user).order_by('-start_date')
    educations = Education.objects.filter(user=request.user).order_by('-start_date')
    projects = Project.objects.filter(user=request.user).order_by('-start_date')
    technical_skills = TechnicalSkill.objects.filter(user=request.user).order_by('category', 'name')
    certifications = Certification.objects.filter(user=request.user).order_by('-issue_date')
    awards = Award.objects.filter(user=request.user).order_by('-date_received')
    languages = Language.objects.filter(user=request.user).order_by('name')
    internships = Internship.objects.filter(user=request.user).order_by('-start_date')
    references = Reference.objects.filter(user=request.user)
    # Prepare context for PDF generator
    context = {
        'resume': resume,
        'personal_info': personal_info,
        'work_experiences': work_experiences,
        'educations': educations,
        'projects': projects,
        'technical_skills': technical_skills,
        'certifications': certifications,
        'awards': awards,
        'languages': languages,
        'internships': internships,
        'references': references,
    }
    from .utils import generate_pdf_resume
    return generate_pdf_resume(context, resume.template)

@login_required
def export_docx(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
    # Gather user data
    personal_info = PersonalInfo.objects.filter(user=request.user).first()
    work_experiences = WorkExperience.objects.filter(user=request.user).order_by('-start_date')
    educations = Education.objects.filter(user=request.user).order_by('-start_date')
    skills = TechnicalSkill.objects.filter(user=request.user).order_by('category', 'name')
    # Prepare context for docx generator
    context = {
        'resume': resume,
        'personal_info': personal_info,
        'work_experiences': work_experiences,
        'educations': educations,
        'technical_skills': skills,
    }
    from .utils import generate_docx_resume
    return generate_docx_resume(context, resume.template)

@login_required
def reference_list(request):
    check = require_resume(request)
    if check: return check
    references = Reference.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'resume_builder/reference_list.html', {'references': references})

@login_required
def reference_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            reference = form.save(commit=False)
            reference.user = request.user
            reference.save()
            messages.success(request, 'Reference added successfully!')
            return redirect('reference_list')
    else:
        form = ReferenceForm()
    return render(request, 'resume_builder/reference_form.html', {'form': form, 'title': 'Add Reference'})

@login_required
def reference_update(request, pk):
    reference = get_object_or_404(Reference, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReferenceForm(request.POST, instance=reference)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reference updated successfully!')
            return redirect('reference_list')
    else:
        form = ReferenceForm(instance=reference)
    return render(request, 'resume_builder/reference_form.html', {'form': form, 'title': 'Edit Reference'})

@login_required
def reference_delete(request, pk):
    reference = get_object_or_404(Reference, pk=pk, user=request.user)
    if request.method == 'POST':
        reference.delete()
        messages.success(request, 'Reference deleted successfully!')
        return redirect('reference_list')
    return render(request, 'resume_builder/reference_confirm_delete.html', {'reference': reference})

@login_required
def internship_list(request):
    check = require_resume(request)
    if check: return check
    internships = Internship.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'resume_builder/internship_list.html', {'internships': internships})

@login_required
def internship_create(request):
    check = require_resume(request)
    if check: return check
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            internship = form.save(commit=False)
            internship.user = request.user
            internship.save()
            messages.success(request, 'Internship added successfully!')
            return redirect('internship_list')
    else:
        form = InternshipForm()
    return render(request, 'resume_builder/internship_form.html', {'form': form, 'title': 'Add Internship'})

@login_required
def internship_update(request, pk):
    internship = get_object_or_404(Internship, pk=pk, user=request.user)
    if request.method == 'POST':
        form = InternshipForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
            messages.success(request, 'Internship updated successfully!')
            return redirect('internship_list')
    else:
        form = InternshipForm(instance=internship)
    return render(request, 'resume_builder/internship_form.html', {'form': form, 'title': 'Edit Internship'})

@login_required
def internship_delete(request, pk):
    internship = get_object_or_404(Internship, pk=pk, user=request.user)
    if request.method == 'POST':
        internship.delete()
        messages.success(request, 'Internship deleted successfully!')
        return redirect('internship_list')
    return render(request, 'resume_builder/internship_confirm_delete.html', {'internship': internship})

@login_required
def resume_classic_preview(request):
    personal_info = PersonalInfo.objects.filter(user=request.user).first()
    work_experiences = WorkExperience.objects.filter(user=request.user).order_by('-start_date')
    educations = Education.objects.filter(user=request.user).order_by('-start_date')
    skills = TechnicalSkill.objects.filter(user=request.user)
    internships = Internship.objects.filter(user=request.user).order_by('-start_date') if 'Internship' in globals() else []
    references = Reference.objects.filter(user=request.user)
    return render(request, 'resume_builder/resume_template_classic.html', {
        'personal_info': personal_info,
        'work_experiences': work_experiences,
        'educations': educations,
        'skills': skills,
        'internships': internships,
        'references': references,
    })

@login_required
def resume_delete(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted successfully!')
        return redirect('resume_list')
    messages.error(request, 'Invalid request.')
    return redirect('resume_list')
