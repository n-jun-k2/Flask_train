from sqlalchemy import create_engine

engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8')

with engine.connect() as con:
    print("connect...")