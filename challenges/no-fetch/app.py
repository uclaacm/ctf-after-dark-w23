from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    content = request.args.get('content') or request.form['content']
    if content is None:
        return render_template('post.html', content='You must provide a content parameter!')
    if content.find('fetch') != -1:
        return render_template('post.html', content='Haha, no fetch for you! ;D')
    return render_template('post.html', content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)