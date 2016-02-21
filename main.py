import psycopg2
conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()


def read_file():
    with open("stats_text_file") as infile:
        data = infile.readlines()
    return [line.replace('\n', '').split(",") for line in data]


print("You can search for receiving stats about any players from the 2015 UGA Bulldogs. \n")
print("Categories you can search by are player name, receptions, receiving yards, touchdowns, or position.")


while True:
    search_or_add = input("Would you like to search the database or add new information to it? Enter either s or a. ")

    if search_or_add == "s":
        search_direction = input("\n" + "To search by player name, enter 'pn'. Receptions, enter 'rec'. Rec yards, enter 'ry'. Touchdowns, 'tds'. Position, 'pos'. ")

        if search_direction == "pn":
            print("")
            player_search = input("Which player do you want to search for? Ex: Malcolm Mitchell can be searched using MMitchell. ")
            cur.execute("select * from player_stats where player_name = (%s);",(player_search,))
            player_results = cur.fetchall()

            if player_results == []:
                print("Sorry no player by that name was found.")
                while True:
                    whole_db = input("Would you like to see the entire player database? Enter y or n. ")

                    if whole_db == "y":
                        cur.execute("select * from player_stats")
                        show_whole_db = cur.fetchall()
                        for player in show_whole_db:
                            print("\n" + "Player Name:" + "\t", "\t", "\t", player[0])
                            print("Receptions:" + "\t", "\t", "\t", "\t", "\t", player[1])
                            print("Receiving Yards:" + "\t", "\t", "\t", player[2])
                            print("Touchdowns:" + "\t", "\t", "\t", "\t", "\t", player[3])
                            print("Position:" + "\t", "\t", "\t", "\t", "\t", player[4])
                            print("")
                        break

                    elif whole_db == "n":
                        break

                    else:
                        print("Sorry, you must enter either y or n.")
                        continue

            else:
                for player in player_results:
                    print("\n" + "Player Name:" + "\t", "\t", "\t", player[0])
                    print("Receptions:" + "\t", "\t", "\t", "\t", "\t", player[1])
                    print("Receiving Yards:" + "\t", "\t", "\t", player[2])
                    print("Touchdowns:" + "\t", "\t", "\t", "\t", "\t", player[3])
                    print("Position:" + "\t", "\t", "\t", "\t", "\t", player[4])
                    print("")

        elif search_direction == "pos":
            print("")
            search_by_position = input("Enter either wr, te, or rb to see the players at that position. ")
            cur.execute("select player_name from player_stats where position = (%s);",(search_by_position,))
            pos_results = cur.fetchall()
            print("Players who are a " + search_by_position + ":")
            for position in pos_results:
                print(position[0])

        elif search_direction == "rec":
            while True:
                print("")
                rec_options = input("Enter either greater than '>' or less than '<' to sort players by receptions? ")

                if rec_options == ">":
                    search_by_min_receptions = input("Enter a minimum number of receptions to see the players who caught more passes than that amount. ")
                    cur.execute("select player_name from player_stats where receptions >= (%s);",(search_by_min_receptions,))
                    rec_ops_1 = cur.fetchall()
                    print("Players who have more than " + search_by_min_receptions + " receptions:")
                    for player in rec_ops_1:
                        print(player[0])
                    break
                
                elif rec_options == "<":
                    search_by_max_receptions = input("Enter a maximum number of receptions to see the players who caught less passes than that amount. ")
                    cur.execute("select player_name from player_stats where receptions <= (%s);",(search_by_max_receptions,))
                    rec_ops_2 = cur.fetchall()
                    print("Players who have less than " + search_by_max_receptions + " receptions:")
                    for player in rec_ops_2:
                        print(player[0])
                    break

                else:
                    print('Not a valid choice.')
                    continue

        elif search_direction == "ry":

            while True:
                print("")
                rec_yard_options = input("Do you want to sort by players with greater than '>' or '<' a certain number of receiving yards? ")

                if rec_yard_options == ">":
                    search_by_min_yards = input("Enter a minimum number of receiving yards to see the players who had more yards than that. ")
                    cur.execute("select player_name from player_stats where receiving_yards >= (%s);",(search_by_min_yards,))
                    rec_yards_1 = cur.fetchall()
                    print("Players who have more than " + search_by_min_yards + " receiving yards:")

                    for player in rec_yards_1:
                        print(player[0])
                    break

                elif rec_yard_options == "<":
                    search_by_max_yards = input("Enter a maximum number of receiving yards to see the players who had less yards than that. ")
                    cur.execute("select player_name from player_stats where receiving_yards <= (%s);",(search_by_max_yards,))
                    rec_yards_2 = cur.fetchall()
                    print("Players who have less than " + search_by_max_yards + " receiving yards:")

                    for player in rec_yards_2:
                        print(player[0])
                    break

                else:
                    print('Not a valid choice.')
                    continue

        elif search_direction == "tds":
            while True:
                print("")
                td_options = input("Do you want to sort by players with greater than '>' or '<' a certain number of touchdowns? ")

                if td_options == ">":
                    search_by_min_tds = input("Enter a minimum number of touchdowns to see the players who scored less than that. ")
                    cur.execute("select player_name from player_stats where touchdowns >= (%s);",(search_by_min_tds,))
                    tds_1 = cur.fetchall()
                    print("Players who have more than " + search_by_min_tds + " touchdowns:")
                    for player in tds_1:
                        print(player[0])
                    break

                elif td_options == "<":
                    search_by_max_tds = input("Enter a maximum number of touchdowns to see the players who scored less than that. ")
                    cur.execute("select player_name from player_stats where touchdowns <= (%s);",(search_by_max_tds,))
                    tds_2 = cur.fetchall()
                    print("Players who have less than " + search_by_max_tds + " touchdowns:")
                    for player in tds_2:
                        print(player[0])
                    break

                else:
                    print('Not a valid choice.')
                    continue

        else:
            print("Sorry that's not a valid search option.")

    elif search_or_add == "a":

        while True:
            new_player = input("To add a player to the database, enter the new player name in format MMitchell for Malcolm Mitchell: ")

            if len(new_player) <= 50:
                valid_new_player = new_player

            else:
                print("Sorry, player name must be less than  or equal to 50 characters. ")
                continue
            new_receptions = input("Enter how many receptions the player had in the 2015 season: ")

            if len(new_receptions) <= 3:
                valid_new_receptions = new_receptions

            else:
                print("Sorry, number of receptions must be less than or equal to 3 characters. ")
                continue
            new_rec_yards = input("Enter how many receiving yards the player had in the 2015 season: ")

            if len(new_rec_yards) <= 4:
                valid_new_rec_yards = new_rec_yards

            else:
                print("Sorry, number of receiving yards must be less than or equal to 4 characters. ")
                continue
            new_tds = input("Enter how many touchdowns the player had in the 2015 season: ")

            if len(new_tds) <= 2:
                valid_new_tds = new_tds

            else:
                print("Sorry, number of touchdowns must be less than or equal to 2 characters. ")
                continue
            new_position = input("Enter the player's position. Must be either 'wr', 'te', or 'rb': ")

            if len(new_position) <= 3:
                valid_new_position = new_position

            else:
                print("Sorry, position must be less than or equal to 3 characters. (Wr, te, or rb. ")
                continue

            cur.execute("insert into player_stats values (%s, %s, %s, %s, %s);", (valid_new_player, valid_new_receptions, valid_new_rec_yards, valid_new_tds, valid_new_position))
            conn.commit()
            print("Awesome, " + new_player + " was added to the database!")
            break


cur.close()
conn.close()