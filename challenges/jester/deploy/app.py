from flask import Flask, render_template, request, make_response
import os
import random
import math
import hashlib

num1 = 0
num2 = 0
a = 0
b = 0
c = 0

from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def update_nums(): 
    global num1, num2, a, b, c
    num1 = random.randint(0, 10000)
    num2 = random.randint(0, 10000)
    a = random.randint(0, 100)
    b = random.randint(0, 10000)
    c = random.randint(0, 10000)
    while a == 0 or (b*b - 4 * a * c) <= 0:
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
        c = random.randint(0, 10000)

rt = RepeatedTimer(1, update_nums)

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    global num1, num2
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/validate', methods = ['POST', 'GET'])
def validate():
    global num1, num2, a, b, c
    try:
        if request.cookies.get('part2') == hashlib.sha256(b"True").hexdigest():
            if request.method == "POST":
                ans1 = request.form.get("answer1")
                ans2 = request.form.get("answer2")
                real_ans1 = round((-1 * b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
                real_ans2 = round((-1 * b - math.sqrt(b * b - 4 * a * c)) / (2 * a))
                try:
                    ans1 = int(ans1)
                    ans2 = int(ans2)
                except:
                    return render_template('part2.html', a=a, b=b, c=c, error="Sorry, that is not an integer")
                if real_ans1 not in [ans1, ans2] or real_ans2 not in [ans1, ans2]:
                    error_msg = "Sorry, the roots of " + str(a) + " x^2 + " + str(b) + " x + " + str(c) + " are not equal to " + str(ans1) + " and " + str(ans2)
                    return render_template('part2.html', a=a, b=b, c=c, error=error_msg)
                return render_template('success.html')
            return render_template('part2.html', a=a, b=b, c=c, error=error_msg)
        else:
            if request.method == "POST":
                answer = request.form.get("answer")
                if answer != None:
                    if not answer.isdigit():
                        return render_template('index.html', num1=num1, num2=num2, error="Sorry, that is not an integer")
                    if int(answer) != num1 + num2:
                        error_msg = "Sorry, " + str(num1) + " + " + str(num2) + " is not equal to " + str(answer)
                        return render_template('index.html', num1=num1, num2=num2, error=error_msg)
                    resp = make_response(render_template('part2.html', a=a, b=b, c=c))
                    resp.set_cookie('part2', hashlib.sha256(b"True").hexdigest())
                    return resp
        return render_template('index.html', num1=num1, num2=num2)
    except:
        return render_template('index.html', num1=num1, num2=num2)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=False, host='0.0.0.0', port=port)