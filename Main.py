import os
import time
from classes import ProductMenu, OrderMenu, CourierMenu

product_menu = ProductMenu()
courier_menu = CourierMenu()
order_menu = OrderMenu()

def MainMenu():
    terminate = False

    print("Welcome to my CLI Program for a Pop up Cafe")
    while terminate is False:
        print(":::::::::::::Main Menu:::::::::::::::::::::;")
        User_Option = input("""Enter a Value
            \n 0 : Exit 
            \n 1 : Menu 
            \n 2 : Order Menu 
            \n 3 : Courier Menu \n""")
        while User_Option !="0":
            if User_Option == "1":
                product_menu.Display_Product_Menu()
            elif User_Option == "2":
                order_menu.Show_order_menu()
            elif User_Option == "3":
                courier_menu.Display_Courier_Menu()
            elif User_Option == "0":
                product_menu.Save_to_csv()
                courier_menu.Save_to_csv()
                order_menu.Save_to_csv()
                terminate = True
                os.system("cls")
                print("\nThanks For Visiting \n")
            else:
                print("Invalid option")
                time.sleep(2)

MainMenu()
