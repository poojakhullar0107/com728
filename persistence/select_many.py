import sqlite3


def retrieve_bot(number_of_bots):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql = "SELECT * FROM bots"
    cursor.execute(sql)
    if number_of_bots is None:
        records = cursor.fetchall()
    else:
        records = cursor.fetchmany(number_of_bots)
    db.close()
    for record in records:
        print(record)


def run():
    print("First three bots in the system")
    retrieve_bot(3)


if __name__ == "__main__":
    run()
