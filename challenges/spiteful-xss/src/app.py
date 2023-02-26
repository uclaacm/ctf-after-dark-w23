from flask import Flask, request, render_template, Response, redirect
import os
import redis
from uuid import uuid4

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "127.0.0.1"), port=int(os.environ.get("REDIS_PORT", "6379")), db=int(os.environ.get("REDIS_DB", "0")))

@app.route("/flag", methods=["GET"])
def get_flag():
    # admin bot has the adminpw cookie with HttpOnly and SameSite=Lax
    if os.environ.get("ADMINPW") == request.cookies.get("adminpw"):
        return os.environ.get("FLAG")
    else:
        return ("no flag for you >:(", 400)

@app.route("/post", methods=["POST"])
def make_post():
    content = request.form.get("content", "")
    if len(content) == 0 or len(content) > 2048:
        return ("Content must be 1-2048 chars, inclusive", 400)
    pid = str(uuid4())
    r.set(pid, content, ex=60 * 60 * 4)
    return redirect(f"/post/{pid}", code=302)

@app.route("/post/<pid>", methods=["GET"])
def view_post(pid):
    content = r.get(pid).decode("utf8")
    if content is None:
        return ("Post not found", 404)
    return render_template("post.html", content=content)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
