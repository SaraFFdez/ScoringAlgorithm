from django.urls import path
from . import views

urlpatterns = [
    path("printScore/", views.print_score_A)
]