import objects

def simulation():
    #create a match
    #create a set
    rotation_1_A = [objects.Player("Sara Fdez", 10), objects.Player("Mau suzuki", 8),objects.Player("Karolina", 6),objects.Player("Guilia", 22),objects.Player("Vinnie", 9),objects.Player("Simona", 11)]
    rotation_1_B = [objects.Player("Sara Fdez", 10), objects.Player("Mau suzuki", 8),objects.Player("Karolina", 6),objects.Player("Guilia", 22),objects.Player("Vinnie", 9),objects.Player("Simona", 11)]
    newMatch = objects.VolleyballMatch(max_sets=3,name_A="Onyx",name_B="Phoenix") #have a different one for abbreviations?
    current_set = objects.VolleyballSet(3,rotation_1_A,rotation_1_B,"A")
    while True:
        whoWon = input("Who won? A or B")
        current_set.updateScore(whoWon)
        current_set.printScore()
        if current_set.won != None:
            print("Set was won by " + current_set.won)
            newMatch.updateSets(current_set.won,current_set)
            newMatch.printSets()
            del current_set
            
            #would have to wait for new rotation and TIMER CHANGE SERVER
            current_set = objects.VolleyballSet(3,rotation_1_A,rotation_1_B,"A") #change server
            print(newMatch.winner)
            if newMatch.winner != None:
                print("Match won by " + newMatch.winner)
                break

simulation()