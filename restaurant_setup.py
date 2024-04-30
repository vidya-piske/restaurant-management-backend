import sqlite3

# Function to create a new SQLite database
def create_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.close()
    print(f"Database '{database_name}' created successfully.")

# Function to create a table for menu items
def create_menu_table(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # SQL query to create a menu_items table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        category TEXT
    )
    """

    # Execute the SQL query
    cursor.execute(create_table_query)
    conn.commit()

    # Close the connection
    conn.close()
    print("Table 'menu_items' created successfully.")



# Function to add a new menu item to the menu table
def add_menu_item(database_name, item_name, price, description="", category=""):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # SQL query to insert a new menu item into the menu_items table
    insert_query = """
    INSERT INTO menu_items (item_name, price, description, category)
    VALUES (?, ?, ?, ?)
    """

    # Execute the SQL query with parameters
    cursor.execute(insert_query, (item_name, price, description, category))
    conn.commit()

    # Close the connection
    conn.close()
    print("Menu item added successfully.")
    
    

# Function to retrieve all menu items from the menu table
def get_all_menu_items(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # SQL query to select all rows from the menu_items table
    select_query = """
    SELECT * FROM menu_items
    """

    # Execute the SQL query
    cursor.execute(select_query)

    # Fetch all rows
    menu_items = cursor.fetchall()

    # Close the connection
    conn.close()

    return menu_items



# Function to update a menu item in the menu table
def update_menu_item(database_name, item_id, new_item_name=None, new_price=None, new_description=None, new_category=None):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Generate SET clause dynamically based on provided parameters
    set_clause = ""
    values = []

    if new_item_name:
        set_clause += "item_name = ?, "
        values.append(new_item_name)
    if new_price:
        set_clause += "price = ?, "
        values.append(new_price)
    if new_description:
        set_clause += "description = ?, "
        values.append(new_description)
    if new_category:
        set_clause += "category = ?, "
        values.append(new_category)

    # Remove the trailing comma and space from the set clause
    set_clause = set_clause.rstrip(", ")

    # SQL query to update the menu item
    update_query = f"""
    UPDATE menu_items
    SET {set_clause}
    WHERE id = ?
    """

    # Add item_id to the values list
    values.append(item_id)

    # Execute the SQL query with parameters
    cursor.execute(update_query, values)
    conn.commit()

    # Close the connection
    conn.close()
    print("Menu item updated successfully.")
    

# Function to delete a menu item from the menu table
def delete_menu_item(database_name, item_id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # SQL query to delete the menu item with the specified ID
    delete_query = """
    DELETE FROM menu_items
    WHERE id = ?
    """

    # Execute the SQL query with the item_id as a parameter
    cursor.execute(delete_query, (item_id,))
    conn.commit()

    # Close the connection
    conn.close()
    print("Menu item deleted successfully.")

# Example usage
# database_name = "restaurant_management.db"
# delete_menu_item(database_name, item_id=1)


# Example usage
# database_name = "restaurant_management.db"
# update_menu_item(database_name, item_id=1, new_price=5.99, new_description="Classic checken burger with cheese and bacon")


# # Example usage
# database_name = "restaurant_management.db"
# menu_items = get_all_menu_items(database_name)
# for item in menu_items:
#     print(item)



# # Example usage
database_name = "restaurant_management.db"
# add_menu_item(database_name, "Veg Burger", 10.99, "Classic Veg burger with cheese", "Main Course")
# add_menu_item(database_name, "Chicken Burger", 11.99, "Classic chicken burger with cheese", "Main Course")
# add_menu_item(database_name, "Egg Burger", 12.99, "Classic Egg burger with cheese", "Main Course")
# add_menu_item(database_name, "Cheese Burger", 13.99, "Classic Cheese burger with cheese", "Main Course")
# add_menu_item(database_name, "Spicy Burger", 14.99, "Classic Spicy burger with cheese", "Main Course")

# # Example usage
# database_name = "restaurant_management.db"
# create_database(database_name)
# create_menu_table(database_name)
# Function to delete menu items by category
def delete_menu_items_by_category(category):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()


    # SQL query to delete menu items with the specified category
    delete_query = """
    DELETE FROM menu_items
    WHERE category = ?
    """

    # Execute the SQL query with the category as a parameter
    cursor.execute(delete_query, (category,))
    conn.commit()

    # Close the connection
    conn.close()
    print({"message": f"All menu items with category '{category}' deleted successfully"})

delete_menu_items_by_category("Test")


