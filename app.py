from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def fetchData():
    db = sqlite3.connect('item.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM data_table')  
    rows = cur.fetchall()  
    db.close()
    return rows 

@app.route('/')
def home():
    data = fetchData()  
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
