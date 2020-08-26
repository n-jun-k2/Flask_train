from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', title='flask test', name=name)

app.run(host='0.0.0.0', port=5000, debug=True)