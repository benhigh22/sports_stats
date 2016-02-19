import psycopg2
conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()

def read_file():
    with open("stats_text_file") as infile:
        data = infile.readlines()
    return [line.replace('\n','').split(",") for line in data]

print("You can search for receiving stats about any players from the 2015 UGA Bulldogs. \n")
print("Categories you can search by are player name, receptions, receiving yards, touchdowns, or position. \n")
while True:
    search_direction = input("To search by player name, enter 'pn'. Receptions, enter 'rec'. Rec yards, enter 'ry'. Touchdowns, 'tds'. Position, 'pos'. ")
    if search_direction == "pn":
        player_search = input("Which player do you want to search for? Ex: Malcolm Mitchell can be searched using MMitchell. ")
        cur.execute("select * from player_stats where player_name = (%s);",(player_search,))
        print(cur.fetchall())
    elif search_direction == "pos":
        search_by_position = input("Enter either wr, te, or rb to see the players at that position. ")
        cur.execute("select player_name from player_stats where position = (%s);",(search_by_position,))
        print(cur.fetchall())
    elif search_direction == "rec":
        while True:
            rec_options = input("Do you want to sort by players with greater than '>' or '<' a certain number of receptions? ")
            if rec_options == ">":
                search_by_min_receptions = input("Enter a minimum number of receptions to see the players who caught more passes than that amount. ")
                cur.execute("select player_name from player_stats where receptions >= (%s);",(search_by_min_receptions,))
                print(cur.fetchall())
                break
            elif rec_options == "<":
                search_by_max_receptions = input("Enter a maximum number of receptions to see the players who caught less passes than that amount. ")
                cur.execute("select player_name from player_stats where receptions <= (%s);",(search_by_max_receptions,))
                print(cur.fetchall())
                break
            else:
                print('Not a valid choice.')
                continue
    elif search_direction == "ry":
        while True:
            rec_yard_options = input("Do you want to sort by players with greater than '>' or '<' a certain number of receiving yards? ")
            if rec_yard_options == ">":
                search_by_min_yards = input("Enter a minimum number of receiving yards to see the players who had more yards than that. ")
                cur.execute("select player_name from player_stats where receiving_yards >= (%s);",(search_by_min_yards,))
                print(cur.fetchall())
                break
            elif rec_yard_options == "<":
                search_by_max_yards = input("Enter a maximum number of receiving yards to see the players who had less yards than that. ")
                cur.execute("select player_name from player_stats where receiving_yards <= (%s);",(search_by_max_yards,))
                print(cur.fetchall())
                break
            else:
                print('Not a valid choice.')
                continue
    elif search_direction == "tds":
        while True:
            td_options = input("Do you want to sort by players with greater than '>' or '<' a certain number of receiving yards? ")
            if td_options == ">":
                search_by_min_tds = input("Enter a minimum number of touchdowns to see the players who scored less than that. ")
                cur.execute("select player_name from player_stats where touchdowns >= (%s);",(search_by_min_tds,))
                print(cur.fetchall())
                break
            elif td_options == "<":
                search_by_max_tds = input("Enter a maximum number of touchdowns to see the players who scored less than that. ")
                cur.execute("select player_name from player_stats where touchdowns <= (%s);",(search_by_max_tds,))
                print(cur.fetchall())
                break
            else:
                print('Not a valid choice.')
                continue




cur.close()
conn.close()