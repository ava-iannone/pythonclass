class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

p1 = Player("Joe Montana","Quarterback")
p2 = Player("Barry Sanders","Running Back")
p3 = Player("Jerry Rice","Wide Receiver")
p4 = Player("Graham Gano","Kicker")

class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players
t1 = NFLTeam("NFLTeam", [p1, p2, p3, p4])

teamList = [p1, p2, p3, p4]
print(t1.teamName)
print(teamList[0].position, teamList[0].name)
print(teamList[1].position, teamList[1].name)
print(teamList[2].position, teamList[2].name)
print(teamList[3].position, teamList[3].name)