import psycopg2
from main import search_player_name, search_pos, search_rec, search_ry, search_tds, add_func
conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()

print("You can search for receiving stats about any players from the 2015 UGA Bulldogs. \n")
print("Categories you can search by are player name, receptions, receiving yards, touchdowns, or position.")


while True:
    search_or_add = input("\n" + "Would you like to search the database or add new information to it? Enter either s or a. ")

    if search_or_add == "s":
        search_direction = input("\n" + "To search by player name, enter 'pn'. Receptions, enter 'rec'. "
                                        "Rec yards, enter 'ry'. Touchdowns, 'tds'. Position, 'pos'. ")
        if search_direction == "pn":
            search_player_name()

        elif search_direction == "pos":
            search_pos()

        elif search_direction == "rec":
            search_rec()

        elif search_direction == "ry":
            search_ry()

        elif search_direction == "tds":
            search_tds()

        else:
            print("Sorry that's not a valid search option.")

    elif search_or_add == "a":
        add_func()


cur.close()
conn.close()
