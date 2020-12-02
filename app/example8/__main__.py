from flask import Flask, render_template

app = Flask(__name__, \
            root_path='../public', \
            static_folder='vue-basic/static', \
            template_folder='vue-basic')

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000, debug=True)