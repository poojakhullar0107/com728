import sqlite3


def get_bot_id_from_user():
    print("Please Enter bot id")
    bot_id = int(input())
    return (bot_id)


def display_bot_from_db(bot_id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql ="SELECT * FROM bots where id=?"
    values = [bot_id]
    cursor.execute(sql,values)
    record = cursor.fetchone()
    db.close()
    print(record)



def get_bot_details_from_user():
    print("Please Enter the name of the field you want to update")
    field_name = input()
    print("Please enter the new value")
    field_value = int(input())
    return [field_name, field_value]


def update_bot_in_db(bot_id,data):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql = f"UPDATE bots SET {data[0]} = {data[1]} WHERE id = {bot_id}"
    cursor.execute(sql)
    db.commit()
    db.close()
    print("Updated...")


def run():
    bot_id = get_bot_id_from_user()
    display_bot_from_db(bot_id)
    data = get_bot_details_from_user()
    update_bot_in_db(bot_id, data)





if __name__ == "__main__":
    run()
