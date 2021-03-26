import database
def menu():
    print("Please select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display Supplier")
    print("[3] Display Supplier locations")
    choice = int(input(" Your Choice : "))
    if choice == 1:
        database.display_products_with_stock_levels()
    elif choice == 2:
        database.display_product_supplier()
    elif choice == 3:
        database.display_product_supplier_locations()
menu()