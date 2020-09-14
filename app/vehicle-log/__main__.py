import datetime
from sqlalchemy import create_engine
from flask import Flask, render_template, request, redirect
from vehicle.insert_query import insert_query

app = Flask(__name__)

engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8mb4')

@app.route("/save",methods=['POST'])
def save():
    """ 記録用URL
    """
    str_start_point = request.form.get("start_point")
    str_finish_point = request.form.get("finish_point")
    str_memo = request.form.get("memo")
    

    app.logger.debug(str_start_point)
    app.logger.debug(str_finish_point)
    app.logger.debug(str_memo)

    query = insert_query('vehicle', str_start_point, str_finish_point, str_memo, datetime.datetime.now())
    app.logger.debug(query)
    
    try:
        if not str_start_point or not str_finish_point:
            raise RuntimeError('Some of the required fields were None')
        with engine.connect() as con:
            con.execute(query)
    finally:
        return redirect("/")

@app.route("/")
def main_page():
    with engine.connect() as con:
        select_result = con.execute("SELECT start, finish, memo, create_at FROM vehicle;")

    log_list = []
    for log in select_result:
        log_list.append((log[0], log[1], log[2] if log[2] is not None else '', str(log[3])))
    return render_template("index.html", log_list=log_list)

app.run(host='0.0.0.0', port=5000, debug=True)