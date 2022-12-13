class VolleyballMatch():
    wins_A = 0
    wins_B = 0

    winner = None

    sets_played = [] #list of sets (this is for info keeping, but is it necessary?)

    total_tout = 0
    total_subs= 0
    total_time = 0

    def __init__(self, max_sets: int, name_A:str, name_B:str):
        self.max_sets = max_sets
        self.name_A = name_A
        self.name_B = name_B

    def checkWinner(self):
        sets_needed = (self.max_sets//2 + 1)
        if self.wins_A == sets_needed:
            self.winner = "A"
        elif self.wins_B == sets_needed:
            self.winner = "B"

    def updateSets(self, whoWon:str, set): #change to a try except
        if whoWon.upper() == "A":
            self.wins_A += 1
            self.sets_played.append(set)
            self.checkWinner()
        elif whoWon.upper() == "B":
            self.wins_B += 1
            self.sets_played.append(set)
            self.checkWinner()
        else:
            print("ERROR WRONG TEAM INPUTTED")
    
    def printSets(self):
        print(f"A | {self.wins_A} : {self.wins_B} | B")
        

class VolleyballSet():
    points_A = 0
    points_B = 0

    tout_A = 0
    tout_B = 0

    start_time = 0 #change later
    end_time = 0 #change later
    duration = 0 #change later

    won = None

    def __init__(self, max_points:int, rotation_A:list , rotation_B:list, server_team:str):
        self.max_points = max_points
        #subs
        self.rotation_A = rotation_A
        self.rotation_B = rotation_B

        self.server_team = server_team
    
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

    def updateScore(self, whoWon:str): #try - except change
        if whoWon.upper() == "A":
            self.points_A += 1
            self.checkWinner()
        elif whoWon.upper() == "B":
            self.points_B += 1
            self.checkWinner()
        else:
            print("ERROR WRONG TEAM INPUTTED")
    
    def printScore(self):
        print(f"A | {self.points_A} : {self.points_B} | B")
    
    def currentServer(self):
        if self.server_team == "A":
            print("The current server for team " + self.server_team + " is player number " + self.rotation_A[0])
        elif self.server_team == "B":
            print("The current server for team " + self.server_team + " is player number " + self.rotation_B[0])

    def updateServer(self, whoWon):
        if self.server_team != whoWon:
            if self.server_team == "A":
                self.server_team = "B"
                self.rotation_B = self.rotation_B[1:] + self.rotation_B[:1]
            elif self.server_team == "B":
                self.server_team = "A"
                self.rotation_A = self.rotation_A[1:] + self.rotation_A[:1]
            else:
                print("Something went wrong")

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