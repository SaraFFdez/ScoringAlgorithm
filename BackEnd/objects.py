class VolleyballMatch():
    wins_A = 0
    wins_B = 0

    winner = None

    total_tout = 0
    total_subs= 0
    total_time = 0
    
    def __init__(self, max_sets: int, name_A:str, name_B:str):
        self.max_sets = max_sets
        self.name_A = name_A
        self.name_B = name_B


    def updateSets(self, whoWon):
        if whoWon == "A":
            self.wins_A += 1
        elif whoWon == "B":
            self.wins_B += 1
        else:
            print("ERROR WRONG TEAM INPUTTED")
    
    def checkWinner(self):
        if self.wins_A == (self.max_sets//2 + 1):
            self.winner == "A"
        elif self.wins_B == (self.max_sets//2 + 1):
            self.winner == "B"

class Set():
    points_A = 0
    points_B = 0

    tout_A = 0
    tout_B = 0

    start_time = 0 #change later
    end_time = 0 #change later
    duration = 0 #change later

    server_number = 0
    won = None

    def __init__(self, max_points:int, rotation_A:list , rotation_B:list, server_team:str):
        self.max_points = max_points
        #subs
        self.rotation_A = rotation_A
        self.rotation_B = rotation_B

        self.server_team = server_team
    
    def updateScore(self, whoWon:str):
        if whoWon == "A":
            self.points_A += 1
        elif whoWon == "B":
            self.points_B += 1
        else:
            print("ERROR WRONG TEAM INPUTTED")

    def checkWinner(self):
        
        if self.points_A == self.max_points:
            if self.points_B == (self.points_A - 1): #check for a deuce
                self.max_points += 1
            else:
                self.won = "A"
        elif self.points_B == self.max_points: 
            if self.points_A == (self.points_B - 1): #check for a deuce
                self.max_points += 1
            else:
                self.won = "B"

class Point():
    def __init__(self, winner:str, type_point:int = 0):
        self.winner = winner
        self.type_point = type_point


class Player():
    def __init__(self, full_name:str, number:int):
        self.full_name = full_name
        self.number = number

    def editName(self, newName):
        self.full_name = newName
    
    def editNumber(self, newNumber):
        self.number = newNumber
    
    def __str__(self):
        return f"{self.full_name} ({self.number})"
    

#def __str__(self):
#    return f"{self.name}({self.age})"