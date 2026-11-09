from django.urls import path

from core.views.socle_views import  LabView


urlpatterns = [
    path("lab", LabView.as_view()),
]