
import psycopg2
from main import read_file



conn = psycopg2.connect(user="sports_user", database="sports_stats")
cur = conn.cursor()

cur.execute("DROP TABLE if exists player_stats;")

create_table_string = """
    CREATE TABLE player_stats (
    player_name varchar(50),
    receptions numeric(3),
    receiving_yards numeric(4),
    touchdowns numeric(2),
    position varchar(3)
    )"""


cur.execute(create_table_string)
conn.commit()

insert_template = "INSERT INTO player_stats VALUES (%s,%s,%s,%s,%s)"

roster = read_file()

for player in roster:
    cur.execute(insert_template, player)
    conn.commit()

cur.close()
conn.close()