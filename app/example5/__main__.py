from sqlalchemy import create_engine
from flask import Flask, render_template, request
app = Flask(__name__)

#engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8')

@app.route("/", methods=["GET", "POST"])
def odd_event():
    if request.method == "GET":
        return render_template("input.html", title="test input", request=request.method )
    else:
        odd = ["偶数","奇数"][int(request.form["num"])%2]
        return render_template("result.html", title="test input", request=request.method, num=str(request.form["num"]), print=odd)

app.run(host='0.0.0.0', port=5000, debug=True)