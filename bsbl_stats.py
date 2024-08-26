import sys
import pandas as pd
from pybaseball import pitching_stats, batting_stats, cache

cache.enable() #Makes repeated calls faster

print("This program only works for players that qualified for a specific season.")

while True:
    player = input("Enter a Qualified Player's Full Name: ")
    year = input("Enter a Year That He Played In: ")
    
    try: #Check if year is a number
        year = int(year)
    except:
        print("Error: Please Enter a Year")
        continue

    player = player.lower().rsplit()
    for name in range(len(player)): player[name] = player[name].capitalize()
    player = " ".join(player)
    
    try:
        pstats = pd.DataFrame(pitching_stats(year, year)).sort_index()[["Name", "Team", "G", "Age", "W", "L", "WAR", "ERA", "IP", "SO", "FIP", "WHIP", "xERA", "Pitching+"]]
        bstats = pd.DataFrame(batting_stats(year, year)).sort_index()[["Name", "Team", "G", "Age", "WAR", "AVG", "OBP", "SLG", "OPS", "wRC+", "xwOBA"]]
    except:
        print("Error: Year Not Found. Please Enter Eligible Year")
        continue
    
    found = False
    for num in range(len(pstats)):
        if player == pstats["Name"][num]:
            stats = pstats.iloc[num]
            print("In", year, ",", stats["Name"], "pitched for", stats["Team"], "in his age", stats["Age"], "season.")
            print("In the", year, "season, he was", stats["W"], "-", stats["L"], "in", stats["G"], "G with a", stats["ERA"], "ERA in", stats["IP"], "IP with", stats["SO"], "SO.")
            print("He also had a WHIP of", stats["WHIP"], "and FIP of", stats["FIP"], ".")
            print("Going more in depth,", stats["Name"], "accumulated ", stats["WAR"], "WAR with an xERA of", stats["xERA"], "and a Pitching+ of", stats["Pitching+"])
            print("TLDR;", player, year, "Season Stats: \n")
            print(stats[["WAR", "G", "W", "L", "ERA", "IP", "SO", "FIP", "WHIP", "xERA", "Pitching+"]].to_string())
            found = True

    for num in range(len(bstats)):
        if player == bstats["Name"][num]:
            stats = bstats.iloc[num]
            print("In", year, ",", stats["Name"], "played for", stats["Team"], "in his age", stats["Age"], "season.")
            print("In the", year, "season, he slashed", stats["AVG"], "/", stats["OBP"], "/", stats["SLG"], "in", stats["G"], "G to give him a", stats["OPS"], "OPS.")
            print("Going more in depth,", stats["Name"], "accumulated ", stats["WAR"], "WAR with a wRC+ of", stats["wRC+"], "and an xwOBA of", stats["xwOBA"])
            print("TLDR;", player, year, "Season Stats: \n")
            print(stats[["WAR", "G", "AVG", "OBP", "SLG", "OPS", "wRC+", "xwOBA"]].to_string())
            found = True     
        
    if not found:
        print(player, "did not qualify in the", year, "season.")