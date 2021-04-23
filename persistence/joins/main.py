import database
def menu():
    print("Please select one of the following options:")
    print("[1] Display stock levels")
    print("[2] Display Supplier")
    print("[3] Display Supplier locations")
    print("[4] Display Missing Supplier")
    print("[5] Display missing products")
    print("[6] Display missing data")

    choice = int(input(" Your Choice : "))
    if choice == 1:
        database.display_products_with_stock_levels()
    elif choice == 2:
        database.display_product_supplier()
    elif choice == 3:
        database.display_product_supplier_locations()
    elif choice == 4:
        database.display_products_missing_suppliers()
    elif choice ==5:
        database.display_suppliers_missing_products()
    elif choice ==6:
        database.display_missing_data()
    else:
        print("invalid choice.. Bye")

if __name__=="__main__":
    menu()