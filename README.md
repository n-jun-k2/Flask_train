# Flask_train
flaskを用いた開発の訓練。
# How to run
```bash
# コンテナを立ち上げる。
docker-compose up -d
# pythonコンテナにログイン
docker-compose exec python /bin/bash

# Flaskのスクリプトを起動
python example1
...
```

# connect to database
pythonで接続するときにはDB事に以下のパッケージをインストールしてください。
- Postgres: psycopg2
- Oracle: cx_Oracle
- MySQL: mysqlclient
- SQLite: pysqlite