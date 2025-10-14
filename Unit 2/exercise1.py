import pandas as pd 
import nfl_data_py as nfl

from helperFunctions import get_team_records

schedules = nfl.import_schedules([2024])

print(schedules.columns.tolist())

records = get_team_records(2020)

print(records[('team','wins','losses')])

print(records[['wins']].mean()) # what was the average wins for the years

# find a season where the average wins was below 8.0 in the last 10 years ?

# 2022 - 8.4 wins
# 2020 - 7.9 wins
