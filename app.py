from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE_NAME = "restaurant_management.db"

# Function to create a new SQLite database
def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.close()

# Function to create a table for menu items
def create_menu_table():
    conn = sqlite3.connect(DATABASE_NAME)
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

# Function to add a new menu item to the menu table
def add_menu_item(item_name, price, description="", category=""):
    conn = sqlite3.connect(DATABASE_NAME)
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

# Function to retrieve all menu items from the menu table
def get_all_menu_items():
    conn = sqlite3.connect(DATABASE_NAME)
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
def update_menu_item(item_id, new_item_name=None, new_price=None, new_description=None, new_category=None):
    conn = sqlite3.connect(DATABASE_NAME)
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

# Function to delete a menu item from the menu table
def delete_menu_item(item_id):
    conn = sqlite3.connect(DATABASE_NAME)
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

# Flask API routes
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to Resturant Management Dashboard"

@app.route('/api/menu', methods=['GET'])
def get_menu():
    menu_items = get_all_menu_items()
    return jsonify(menu_items)

@app.route('/api/menu/add', methods=['POST'])
def add_menu():
    data = request.json
    add_menu_item(data['item_name'], data['price'], data.get('description', ""), data.get('category', ""))
    return jsonify({"message": "Menu item added successfully"})

@app.route('/api/menu/update/<int:item_id>', methods=['PUT'])
def update_menu(item_id):
    data = request.json
    update_menu_item(item_id, data.get('item_name'), data.get('price'), data.get('description'), data.get('category'))
    return jsonify({"message": "Menu item updated successfully"})

@app.route('/api/menu/delete/<int:item_id>', methods=['DELETE'])
def delete_menu(item_id):
    delete_menu_item(item_id)
    return jsonify({"message": "Menu item deleted successfully"})

if __name__ == '__main__':
    # create_database()
    # create_menu_table()
    app.run(debug=True)
