import tui
def list_years(data):
    tui.started("Listing years")
    years = set()
    for record in data:
        year = record[9]
        years.add(year)
    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying medals")
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[14]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    tui.display_medal_tally(medal_tally)
    tui.completed()

def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[6]
        medal = record[14]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in medal_tally:
            medal_tally[team][medal] += 1
        else:
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1

    tui.display_team_medal_tally(medal_tally)
    tui.completed()