from functions import product_list_from_csv, get_courier_from_csv,order_list_from_csv
import copy
import csv
import os
import time
import re

class ProductMenu():
    def __init__(self):
        self.product_list = product_list_from_csv()

    def Display_Product_Menu(self):
        from Main import MainMenu
        self.product_list = product_list_from_csv()

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print product list.\n"
                        f"2. Create new product\n"
                        f"3. Update product\n"
                        f"4. Delete product\n")
        if command == '1':
            self.Show_Product_list()
        elif command == '2':
            self.Add_Product()
        elif command == '3':
            self.Update_product()
        elif command == '4':
            self.Delete_product()
        elif command == '0':
            MainMenu()

            
    def Save_to_csv(self):
        header = ["name","price"]
        with open('Products.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.product_list)

    def Show_Product_list(self):
        os.system("cls")
        temp_list = product_list_from_csv()
        for item in temp_list:
            print(item)

    def Add_Product(self):# creats new product
        os.system("cls")
        try:
            new_product_name = input("Please input the name of the new product? ")
            new_product_price = float(input("Please input the price of the new product? "))
            new_item = {'name': new_product_name, 'price': new_product_price}
            # new_item = Product(new_product_name, new_product_price)
            self.product_list.append(new_item)
            print(f"{new_product_name}Product Added")
            self.Save_to_csv()
        except (ValueError, IndexError):
            print('Invalid input.')
            self.Add_Product()

    def Update_product(self):
        os.system("cls")
        temp_list = self.product_list
        for count, value in enumerate(self.product_list):
            print(count + 1, value)
        try:
            thing_to_update = int(input(f'Please pick a product to update: '))

            old_thing = copy.deepcopy(temp_list[thing_to_update - 1])
            new_thing = temp_list[thing_to_update - 1]
            for key in new_thing:
                new_key = input(f'What is the new {key}? ')
                if new_key == '':
                    pass
                else:
                    new_thing[key] = new_key

            temp_list[thing_to_update - 1] = new_thing

            print(f"\n'{old_thing}' is updated to '{new_thing}'\n")
            self.product_list = temp_list
            self.Save_to_csv()
        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.Update_product()

    def Delete_product(self):
        os.system("cls")
        temp_list = self.product_list
        for count, value in enumerate(self.product_list):
            print(count + 1, value)
        try:
            delete_product_item = int(input("""
            Please use the index to pick a product to delete 
            >>>>
            """))
            del temp_list[delete_product_item - 1]
            time.sleep(2)
            self.Save_to_csv()
            print(f"Item {temp_list[int(delete_product_item)]} has been deleted ")
            time.sleep(2)
            self.Display_Product_Menu()
        except (ValueError, IndexError):
            print("Input was not valid")
            self.Delete_product()

class CourierMenu():
    def __init__(self):
        self.courier_list = get_courier_from_csv()
    def Display_Courier_Menu(self):
        from Main import MainMenu
        os.system("cls")
        self.courier_list = get_courier_from_csv()
        choice = input(f"Please enter your command. \n"
                        f"0. Go back to main menu. \n"
                        f"1. Print Courier list. \n"
                        f"2. Create new Courier \n"
                        f"3. Update Courier \n"
                        f"4. Delete Courier \n")
        while True:
            if choice == "0":
                MainMenu()
            elif choice == "1":
                self.Show_courier_list()
            elif choice == "2":
                self.Create_courier()
            elif choice == "3":
                self.Update_courier()
                
            elif choice == "4":
                self.Delete_courier()
            else:
                time.sleep(0.5)
                print("\nPlease only input number as command.\n")
                time.sleep(3)
                CourierMenu()
            break
    def Save_to_csv(self):
        header = ["name","phone"]

        with open('Couriers.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.courier_list)
    def Show_courier_list(self):
        os.system("cls")
        temp_list = get_courier_from_csv()
        for item in temp_list:
            print(item)

    def Create_courier(self):
        os.system("cls")
        try:
            New_Courier_name = input("""
            Please Add Name
            >>>>
            """)
            New_Courier_phone = input("""
            Please Add Phone Number
            >>>>
            """)
            new_courier = {'name': New_Courier_name, 'phone': New_Courier_phone}
            self.courier_list.append(new_courier)
            print("A new courier has been added")
            print(self.courier_list)
            self.Save_to_csv()
        except (ValueError, IndentationError):
            print("Invalid")

    def Update_courier(self):
        os.system("cls")
        temp_list = self.courier_list
        for count, value in enumerate(self.courier_list):
            print(count + 1, value)
        try:
            Courier_to_Update = int(input(f'Please pick Courier to update: '))
            
            previous_courier  = copy.deepcopy(temp_list[Courier_to_Update - 1])
            new_courier = temp_list[Courier_to_Update - 1]
            for key in new_courier:
                newKey = input(f'What is the new {key}? ')
                if newKey == '':
                    pass
                else:
                    new_courier[key] = newKey

            temp_list[Courier_to_Update - 1] = new_courier

            print(f"\n'{previous_courier}' is updated to '{new_courier}'\n")
            self.courier_list = temp_list
            self.Save_to_csv()
        except (ValueError, IndexError):
            print("\n Invalid \n")
            self.Update_courier()

    def Delete_courier(self):
        os.system("cls")
        temp_list = self.courier_list
        for count, value in enumerate(self.courier_list):
            print(count + 1, value)
            courier_to_delete = input(f"""Please pick a product
             to delete """)
            try:
                courier_to_delete = int(courier_to_delete)
            except (ValueError, IndexError):
                time.sleep(1)
                print("invalid input")
                self.Delete_courier()
            del temp_list[courier_to_delete - 1]
            self.Save_to_csv()

class OrderMenu():
    def __init__(self):
        self.order_list = order_list_from_csv()

    def Show_order_menu(self):
        os.system("cls")
        self.order_list = order_list_from_csv()

        OrderMenuOption = input(""" ****ORDERS MENU****
        0: Return to Main Menu
        1: View Order list
        2: Create New Order
        3: Update Order Status
        4: Update Order details 
        5: Delete Order 
        >>>> """)

        if OrderMenuOption == 0:
            pass
        elif OrderMenuOption == "1":
            self.print_order_list()
            time.sleep(3)
        elif OrderMenuOption == "2":
            self.Create_order()
        elif OrderMenuOption == "3":
            self.Update_Order_status()
        elif OrderMenuOption == "4":
            self.Update_Order()
        elif OrderMenuOption == "5":
            self.Delete_Order()
    

    def Save_to_csv(self):
        header = ['customer_name',
                  'customer_address', 'customer_phone',
                  'courier', 'status']
        with open("Orders.csv", "w") as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.order_list)

    def print_order_list(self):
        os.system("cls")
        temp_list = order_list_from_csv()
        for item in temp_list:
            print(item)
    
    def Create_order(self):
        os.system("cls")
        status = "PREPARING"
        try:
            New_Costumer_Name = input("Enter Customer name: ").title()
            New_Costumer_Address = input("""
            Add Address
            >>>>
            """)
            New_Customer_Phone = input("""
            Add Phone
            >>>>
            """)
            Courier_Choice = self.Choose_courier()
            new_order = {'customer_name': New_Costumer_Name,
                            'customer_address': New_Costumer_Address,
                            'customer_phone': New_Customer_Phone,
                            'courier': Courier_Choice,
                            'status': status,
                        }
        
        except (ValueError, IndexError):
            print("Invalid Input")
            self.Create_order()
        self.order_list.append(new_order)
        print("Order Successfully Created")
        self.Save_to_csv()
        time.sleep(1)
        self.Show_order_menu()
    
    def Update_Order(self):
        os.system("cls")
        temp_list = self.print_order_list
        for count, value in enumerate(self.order_list):
            print(count + 1, value)
        try:
            update_order_Index = input("""
            Please use the index to pick an order to update
            >>>>
            """)
            old_order = copy.deepcopy(temp_list[update_order_Index - 1])
            new_order = temp_list[update_order_Index -1]
            for key in new_order:
                newKey = input(f"What is the new {key}? ")
                if newKey == "":
                    pass
                else:
                    new_order[key] = newKey
            temp_list[update_order_Index - 1] = new_order
            print(f"\n'{old_order}' is updated to '{new_order}'\n")
            self.order_list = temp_list
            self.Save_to_csv()
        except (ValueError, IndexError):
            print("Invalid")
            self.Update_Order()
    
    def Update_Order_status(self):
        os.system("cls")
        temp_list = self.order_list
        try:
            for count,value in enumerate(self.order_list):
                print(count + 1, value)
                Update_index = int(input("""Enter the index of the
                                            order you would like to delete"""))
                previous_order = temp_list[Update_index -1]
                new_order = temp_list[Update_index -1]
                command = input(""" Please update the status: \n'
                                    '1. Preparing\n'
                                    '2. Dispached\n'
                                    '3. Delivered\n'
                                    '4. Cancelled\n""")
                if command == 1:
                    command = "Preparing"
                elif command == 2:
                    command = "Dispached"
                elif command == 3:
                    command = "Delivered"
                elif command == 4:
                    command = "Cancelled"
                new_order["status"] = command
                temp_list[Update_index -1] = new_order
                print(f"{previous_order} has been update to {new_order}")
                self.order_list = temp_list
                self.Save_to_csv()
        except (ValueError, IndexError):
            print("The input is invalid")
            self.Update_Order_status()


    def Delete_Order(self):
        os.system("cls")
        temp_list = self.order_list
        for count, value in enumerate(self.order_list):
            print(count + 1, value)
        try:
            Order_delete = input("""
            Please use the index to pick a product to delete
            >>>>
            """)

            del temp_list[Order_delete - 1]
            print("Order deleted")
            self.Save_to_csv()
            self.Show_order_menu()
        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.Delete_Order()

    def Choose_courier(self):
        os.system("cls")
        temp_list = get_courier_from_csv()
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        end_loop = False
        while end_loop is not True:
            choice = input("Enter the index value of the courier")
            if re.match("[0-9]*$", choice):
                return choice
            else:
                print("Invalid Input")
                self.Choose_courier()
    
    def Pick_product(self):
        os.system("cls")
        temp_list = product_list_from_csv()
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        end_loop = False
        while end_loop is not True:
            choice = input("enter the index of the product you want to delete")
            if re.match("[0-9]*$", choice):
                end_loop = True
            else:
                continue
        return choice


    




            








    






    