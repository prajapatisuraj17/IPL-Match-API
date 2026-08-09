import pandas as pd 
import numpy as np

matches=pd.read_csv('ipl-matches.csv')

def get_teams():
    return list(set(matches['Team1']).union(set(matches['Team2'])))


def team_vs_team(team1,team2):
    valid_team=list(set(matches['Team1']).union(set(matches['Team2'])))
    if team1 in valid_team and team2 in valid_team:
      duo_team=matches[(matches['Team1']==team1) & (matches['Team2']==team2) | (data['Team1']==team2) & (data['Team2']==team1)]
      match_won_team1=duo_team['WinningTeam'].value_counts()[team1]
      match_won_team2=duo_team['WinningTeam'].value_counts()[team2]

      total_matches=duo_team.shape[0] 

      draws=total_matches-(match_won_team1 + match_won_team2)

      response={
        'total_matches':total_matches,
        'match_won_team1':int(match_won_team1),
        'match_won_team2':int(match_won_team2),
        'draws':int(draws)
      }

      return response
    else:
      return {'error':'Invalid Team Name'}


def allRecord(team):
    df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)].copy()
    mp = df.shape[0]
    won = df[df.WinningTeam == team].shape[0]
    nr = df[df.WinningTeam.isnull()].shape[0]
    loss = mp - won - nr
    nt = df[(df.MatchNumber == 'Final') & (df.WinningTeam == team)].shape[0]
    return {'matchesplayed': mp,
            'won': won,
            'loss': loss,
            'noResult': nr,
            'title': nt}






