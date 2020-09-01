from sqlalchemy import create_engine

engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8')

with engine.connect() as con:
    rows = con.execute("select * from user;")
    for row in rows:
        print(row)
        print(f"id : {row.id} , password : {row[1]}")