import csv
import sqlite3


def read_data_file(file_path):
    records=[]
    with open (file_path) as file:
        csv_reader=csv.reader(file)
        for line in csv_reader:
            records.append(line)
    return records


def insert_in_db(records):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    for record in records:
        sql = "INSERT INTO bots (name, max_speed, max_strength, date_created, manufacturer_id)\
        VALUES (?,?,?,?,?)"
        values = [record[0], record[1], record[2], record[3], record[4]]
        cursor.execute(sql, values)
    db.commit()
    db.close()


def run():
    print("Please Enter the file path")
    file_path=input()
    records=read_data_file(file_path)
    print("inserting Data into Database.....")
    insert_in_db(records)
    print(f"Done....{len(records)} records inserted")


if __name__ == "__main__":
    run()