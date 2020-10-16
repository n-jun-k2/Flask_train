from flask import Flask, render_template

app = Flask(__name__, \
            root_path='../public', \
            static_folder='vue-app/static', \
            template_folder='vue-app')

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000, debug=True)