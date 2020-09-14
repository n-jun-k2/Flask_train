from sqlalchemy import create_engine
from flask import Flask, render_template, request, redirect
from vehicle.insert_query import insert_query

app = Flask(__name__)

engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8')

@app.route("/save",method=['POST'])

@app.route("/")
def main_page():
    with engine.connect() as con:
        select_result = con.execute("SELECT start, finish, memo, create_at FROM vehicle;")

    log_list = []
    for log in select_result:
        log_list.append((log[0], log[1], log[2] if log[2] is not None else '', str(log[3])))
    return render_template("index.html", log_list=log_list)


app.run(host='0.0.0.0', port=5000, debug=True)