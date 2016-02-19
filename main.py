import psycopg2
conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()

def read_file():
    with open("stats_text_file") as infile:
        data = infile.readlines()
    return [line.replace('\n','').split(",") for line in data]
cur.execute("select * from player_stats")
rows = cur.fetchall()
print(rows[0])
print("You can search for any receiving stats about any players from the 2015 UGA Bulldogs.")
search_direction = input("If you want to search by player name, enter y. Any other entry will give you different search options. ")
if search_direction == "y":
    player_search = input("Which player do you want to search for? ")
    cur.execute("select * from player_stats where player_name = (%s);",(player_search,))
    print(cur.fetchall())
else:
    search_by_position = input("Enter either wr, te, or rb to search for position-specific stats! ")
    cur.execute("select * from player_stats where position = (%s);",(search_by_position,))
    print(cur.fetchall())






cur.close()
conn.close()