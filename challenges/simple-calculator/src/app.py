from flask import Flask, request, render_template, Response
import os

app = Flask(__name__)

@app.route("/flag", methods=["GET"])
def get_flag():
    if 0 == 1:
        return os.environ.get("FLAG")
    else:
        return ("no flag for you >:(", 400)

@app.route("/source", methods=["GET"])
def view_source():
    source = request.args.get("file", "app.py").replace("../", "")
    try:
        with open(source, "r") as f:
            return Response(f.read(), mimetype="text/plain")
    except IOError:
        return ("Could not read file", 500)

@app.route("/", methods=["POST"])
def calculate():
    query = request.form.get("query")
    if query is None:
        return ("Please include a query", 400)
    if query == "1+1":
        result = "2"
    elif query == "2+2":
        result = "4"
    elif query == "1+2":
        result = "3"
    elif query == "1+2*3":
        result = "9"
    else:
        result = "x for some x"
    return render_template("index.html", query=query, result=result)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
