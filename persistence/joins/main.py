import database
def menu():
    print("Please select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display Supplier")
    choice = int(input(" Your Choice : "))
    if choice == 1:
        database.display_products_with_stock_levels()
    if choice == 2:
        database.display_product_supplier()
menu()