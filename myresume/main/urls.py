# main/urls.py
from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    path("", views.ResumeIndex.as_view(), name="index"),
    path("experience/", views.ResumeExperience.as_view(), name="experience"),
    path("education/", views.ResumeEducation.as_view(), name="education"),
    path("skills/", views.ResumeSkills.as_view(), name="skills"),
]