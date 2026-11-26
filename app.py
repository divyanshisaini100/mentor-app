from flask import Flask, render_template
# from flask-sqlalchemy import SQLAlchemy
import sqlite3

# db = SQLAlchemy(app)

def db_connection(){
    conn = None
    try:
        conn = sqlite3.connect("mentor_app.db")
    except sqlite3.Erorr as e:
        print(e)
    return conn    

}

app = Flask(__name__)


@app.route('/')
def login():
    render_template('/login.html')

if __name__ = '__main__':
    app.run(debug=True, port=8000)
