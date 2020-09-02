from sqlalchemy import create_engine

engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8')

with engine.connect() as con:
    before_rows = con.execute("SELECT * FROM USER;")
    print("=== befor ===")
    for row in before_rows:
        print(row)

    insert_rows = [
        {"id": 8, "password": "hogehoge8"},
        {"id": 9, "password": "fugafuga9"}
        ]

    for row in insert_rows:
        query = f"INSERT INTO USER ({','.join(row.keys())}) VALUES {tuple(row.values())}"
        print(query)
        con.execute(query)

    print("=== after ===")
    after_rows = con.execute("SELECT * FROM USER;")
    for row in after_rows:
        print(row)