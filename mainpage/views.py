from django.shortcuts import render
from django.http import HttpResponse
from .models import VolleyballSet, Player, VolleyballMatch
# Create your views here.
def print_score_A(request):
    rotation_1_A = [Player("Sara Fdez", 10), Player("Mau suzuki", 8),Player("Karolina", 6),Player("Guilia", 22),Player("Vinnie", 9),Player("Simona", 11)]
    rotation_1_B = [Player("Sara Fdez", 10), Player("Mau suzuki", 8),Player("Karolina", 6),Player("Guilia", 22),Player("Vinnie", 9),Player("Simona", 11)]
    newMatch = VolleyballMatch(max_sets=3,name_A="Onyx",name_B="Phoenix") #have a different one for abbreviations?
    current_set = VolleyballSet(3,rotation_1_A,rotation_1_B,"A")
    return render(request, "score.html", {"set": current_set})