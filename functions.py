import os
import csv
import re



def product_list_from_csv():
    temp_list = []
    if os.path.exists('Products.csv'):
        with open('Products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list
    else:
        with open('Products.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'price'])
            writer.writerow(['sandwich', '2.0'])
            writer.writerow(['crisp', '0.80'])
            writer.writerow(['coffe', '1.70'])
            writer.writerow(['coffe', '1.70'])
            writer.writerow(['burger', '1.50'])
        with open('Products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list

def get_courier_from_csv():
    temp_list = []
    if os.path.exists('Couriers.csv'):
        with open('Couriers.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list
    else:
        with open('Couriers.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'phone'])
            writer.writerow(['Amazon', '35457425685984'])
            writer.writerow(['FEDEX', '235543935235'])
            writer.writerow(['DPD', '878748787878'])
        with open('Couriers.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list

def order_list_from_csv():
    temp_list = []
    if os.path.exists('Orders.csv'):
        with open('Orders.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list
    else:
        with open('Orders.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['customer_name',
                             'customer_address', 'customer_phone',
                             'courier', 'status', 'items'])
        with open('Orders.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list


