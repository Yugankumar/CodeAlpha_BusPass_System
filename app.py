from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        source TEXT,
        destination TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    email = request.form['email']
    source = request.form['source']
    destination = request.form['destination']

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(name,email,source,destination) VALUES(?,?,?,?)",
        (name, email, source, destination)
    )

    conn.commit()
    conn.close()

    return render_template(
        'dashboard.html',
        name=name,
        source=source,
        destination=destination
    )

if __name__ == '__main__':
    app.run(debug=True)