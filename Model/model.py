from typing import OrderedDict
from json_players import get_obj
from Model.team_calc import calc_team_means

class Model:
    
    boxScoreList = [] # [[team1boxscores], [team2boxscores]]
    
    team1 = []  # [[player1], [player2], ...]
    
    team2 = []  # [[player1], [player2], ...]

    def calculate_box_score(players):
        Model.create_team_profiles(players)
        Model.calculate_team_means(Model.team1, Model.team2)
        
    def create_team_profiles(players): # [[player], [offense], [defense]], bug if teams unequal?
        plaP = 0
        for p in range(len(players.players)): # p is never used
            vitalsPlayer = players.players[plaP]
            #offensePlayer = players.players[plaP].ratings[0].offense[0]
            #defensePlayer = players.players[plaP].ratings[1].defense[0]
            #offAttr = Model.attr_val_list(offensePlayer)
            #defAttr = Model.attr_val_list(defensePlayer)
            if vitalsPlayer.team == 'LAL': # If multiple teams, change this
                Model.team1.append([vitalsPlayer, offAttr, defAttr])
                plaP += 1
            else:
                Model.team2.append([vitalsPlayer, offAttr, defAttr])
                plaP += 1
                
    def calculate_team_means(team1, team2):
        teams = [team1, team2]
        calc_team_means(team1)
        #for t in range(len(teams)):
        #    for pt in range(len(teams[t])):
        #        for ptr in range(len(teams[t][pt])):
        #           print((teams[t][pt][ptr]))
                    

    def attr_val_list(self):
        """This breaks the object and returns a dict again!"""
        kvDict = OrderedDict()
        items = self.__dict__.items()
        for k, v in items:
            kvDict[k] = v
        return kvDict
    
#class PlayerBoxScore(object):
   # name = None
   # fgm, fga, fgp, tpm, tpa, tpp, trb, ast, pts = 0
    
  #  def __init__(self, name, fgm, fga, tpm, tpa, ast):
  #      self.name = name
  #      self.fgm = fgm
  #      self.fga = fga
  #      self.fgp = ""(fgm/fga)*100 + " %"
  #      self.tpm = tpm
  #      self.tpa = tpa
  #      self.tpp = ""(tpm/tpa)*100 + " %"
  #     self.ast = ast
        
  #  def __repr__(self):
  #      pass
        
    
