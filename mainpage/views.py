from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def print_score_A(request):
    return render(request, "score.html", {"score_A": 2, "score_B": 3})