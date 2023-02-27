from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method != 'POST':
        return render_template('index.html', msg='You must POST the restaurant on social media in order to access the menu!')
    if request.headers.get("User-Agent") != 'MenuBrowser':
        return render_template('index.html', msg='Only the elite who used MenuBrowser can access the menu!')
    if request.headers.get("Referer") != 'https://yelp.com':
        return render_template('index.html', msg='Only those who were referred by https://yelp.com can access the menu!')
    return render_template('index.html', msg='flag{jUs1_8_pLa1n_c3e5eBur9eR}')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)