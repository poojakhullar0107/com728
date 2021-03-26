import sqlite3
def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, description, stock.quantity "\
        "from product NATURAL JOIN stock "
    cursor.execute(sql)
    records = cursor.fetchall()
    print(f"There are {len(records)} products in the catalogue")

    for record in records:
        print(f"Product is: {record[0]} \nDescription is :{record[1]}\nQuantity is : {record[2]}\n")

    db.close()

def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name from"\
        " product INNER JOIN supplier "\
        "ON product.supplier_id=supplier.id"
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        print(f"Product is: {record[0]} ;Supplier is : {record[1]}\n")

    db.close()
def  display_product_supplier_locations():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name, "\
            "location.city,location.country from" \
            " product INNER JOIN supplier " \
            "ON product.supplier_id=supplier.id"
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        print(f"Product is: {record[0]} ;Supplier is : {record[1]}\n")

    db.close()