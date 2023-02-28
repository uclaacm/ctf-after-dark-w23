from flask import Flask, render_template, request
from mysql import connector

app = Flask(__name__)

config = {
    'user': 'app',
    'password': 'password',
    'host': 'db',
    'port': 3306,
    'database': 'appdb'
}

@app.route("/", methods=['GET', 'POST'])
def index():
    error = None
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if "--" in user or "--" in password:
            error = "No double dashes! I knew you would try an SQL injection..."
        else:
            connection = connector.connect(**config)
            cur = connection.cursor()
            query = f"SELECT * FROM user WHERE username = '{user}' AND password = '{password}'"
            cur.execute(query)
            rv = [(i,j) for i, j in cur]
            if len(rv) == 0:
                error = "Login Failed"
            else:
                error = rv[0][1]
            cur.close()
            connection.close()
    return render_template("index.html", error=error)