from helperFunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "RB")  
print(stats)

# plot_player_stat(stats, stat="passing_tdy", top_n=20, title="QB Passing touchdowns (2024)", save_path="qb_passing_tdy_2024.png"  )

# 2) One-liner wrapper:
# plot_weekly_player_stats(2024, "WR", stat="receiving_yards", top_n=15, week=[1,2,3], save_path="wr_rec_yards_wk1-3.png")





# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar 
# graphs and answer the following questions.

# 1. Use each helper function to find your own metric to visualize. use the weeklyPlayerStats 
# function to find positions and stat columns by name

stats = weeklyPlayerStats(2024, "QB")
print(stats)

# 2. Find the player with the most touchdowns in 2024?

"Derrick Henry is the player with the most touchdowns in 2024 at 21 touchdowns."

# 3. Find the player with the highest total passing yards in 2024.

"Jared Goff is the player with the highest total passing yards in 2024 at 4942 passing yards."

# 4. Which player had the highest rushing yards in week 1 and in week 17?

"Joe Mixon is the player that had the highest rushing yards in week 1 and in week 17 with 159 yards."