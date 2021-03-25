import sqlite3


def get_bot_from_user():
    print("Please enter the name of the bot:")
    name=input()
    print("Please enter the maximum speed of the bot:")
    max_speed=int(input())
    print("Please enter the maximum strength of the bot:")
    max_strength = int(input())
    print("Please enter the date of manufacture:")
    date_created=input()
    print("Please enter manufacturer id:")
    manufacturer_id=int(input())
    return[name,max_speed,max_strength,date_created,manufacturer_id]


def insert_bot_in_db(bot_details):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql = "INSERT INTO bots (name,max_speed,max_strength,date_created,manufacturer_id) VALUES (?,?,?,?,?)"
    value = [bot_details[0],bot_details[1],bot_details[2],bot_details[3],bot_details[4]]
    cursor.execute(sql,value)
    db.commit()
    print(f"Id. of new record is : {cursor.lastrowid}")
    db.close()


def run():
    bot_details = get_bot_from_user()
    insert_bot_in_db(bot_details)


if __name__ == "__main__":
    run()