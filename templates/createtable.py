import sqlite3

def InsertData():
    item_name = input("Enter item name:")
    quantity = input("Enter quantity:")
    price = input("Enter price:")
    db = sqlite3.connect('../item.db')
    cur = db.cursor()
    cur.execute('INSERT INTO data_table(item_name, quantity, price) VALUES (?,?,?)', (item_name, quantity, price))
    db.commit()
    db.close()
    print("Data Inserted")

def MainMenu():
    print("1. Insert data into db")
    while True:
        user_input = input("Enter a value or ('Q' to quit):")
        if user_input == 'Q':
            break
        elif user_input == '1':
            InsertData()

MainMenu()
