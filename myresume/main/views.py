from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class ResumeIndex(TemplateView):
    template_name = "resume/index.html"

class ResumeExperience(TemplateView):
    template_name = "resume/experience.html"

class ResumeEducation(TemplateView):
    template_name = "resume/education.html"

class ResumeSkills(TemplateView):
    template_name = "resume/skills.html"
