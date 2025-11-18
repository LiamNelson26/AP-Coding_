
from helperLogic import get_player_stats_by_name, plot_weekly_player_stats,plot_player_stat, get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_team_stats
import matplotlib.pyplot as plt

# Columns available to research based on year and position
columnData = get_position_columns(2024, "QB")
# print(columnData)

'1. How much does QB pass accuracy influence team wins ? '
teamRecord = get_team_records(2024)
print(teamRecord)

qbData = weeklyPlayerStats(2024, 'QB')
print(qbData)

'J.Allen'
'J.Hurts'

playerStat= get_player_stats_by_name(2024,'J.Hurts','QB')
print(playerStat)

'Answer: Yes, there is a relationship. based on the average qb completion %, anything above 60 % is considered a good completion number'
"also based on team records, the top 10- top teams all have had qbs that have over 65% completion percentages."


'2. Does defensive turnovers contribute to a teams win percentage? '
teamStats = get_team_stats(2024)
print(teamStats)

def get_team_stats(year):

    print("Catching team statistics for the year {2024}")

    stats = {
        'Team': ['Baltimore Orioles', 'New York Yankees', 'Boston Red Sox', 'Tampa Bay Rays', 'Toronto Blue Jays'],
        'Wins': [101, 95, 88, 85, 80],
        'Losses': [61, 67, 74, 77, 82],
        'Home Runs': [250, 230, 210, 190, 200],
        'ERA': [3.45, 3.60, 3.80, 3.90, 4.10],
    }

    return get_team_stats(2024)


'3. Who has the most passing yards of all time ? '