import database
def menu():
    print("Please select one of the following options:")
    print("[1] Display stock levels")
    choice = int(input())
    print(f"Your selection is :  {choice}")
    if choice == 1 :
        database.display_products_with_stock_levels()
menu()