# Flask_train
flaskを用いた開発の訓練。

# Document list
- [エラーメモ](doc/error_memo.md)
- [CGIの勉強](doc/python-cig.md)
- [Vue.jsについての勉強メモ](doc/vue.md)
- [Vue.jsの作成手順](doc/vue_dev.md)

# How to run

1. Create ``.env`` file.
    ```
    LOCAL_HOST=<ipアドレス>
    ```
2. Enter the following command
    ```bash
    # コンテナを立ち上げる。
    docker-compose up -d

    # Flaskの開発を行う際
    docker-compose exec python /bin/bash
    # Flaskのスクリプトを起動
    python example1

    # vue.jsの開発する際
    docker-compose exec node_js /bin/bash
    # 開発するプロジェクトのディレクトリへ移動(vue-appのプロジェクトに移動)
    cd vue-app
    # packageインストール
    npm install
    # あとは開発後にビルドする。
    npm run build
    ...
    ```

# Connect to WSL2 localhost
Prepare a file ``c:/Users/<user name>/.wslconfig`` on the Windows side and describe as follows.
```
localhostForwarding=True
```
# Connect to the server
```
http://localhost:5000/....
```

# connect to database
pythonで接続するときにはDB事に以下のパッケージをインストールしてください。
- Postgres: psycopg2
- Oracle: cx_Oracle
- MySQL: mysqlclient
- SQLite: pysqlite


# WSL2 permission error
mysqlの構築の際にハマったエラー対応方法(以下の奴ら)
[参考](https://sig9.hatenablog.com/entry/2020/02/19/000000)
```
mysql_1   | mysqld: Cannot change permissions of the file 'private_key.pem' (OS errno 1 - Operation not permitted)
mysql_1   | 2020-09-10T05:04:53.449233Z 0 [ERROR] [MY-010295] [Server] Could not set file permission for private_key.pem
mysql_1   | 2020-09-10T05:04:53.449629Z 0 [ERROR] [MY-010119] [Server] Aborting
```

1. ```/etc/wsl.conf```をWSL2のディストリビューションに作成。

```bash
# wslのディストリビューションにwslの設定ファイルを新規作成
> sudo touch /etc/wsl.conf
# 設定ファイルを編集する。
> vi /etc/wsl.conf
```

2. マウントオプションを変更する。
```
[automount]
options = "metadata"
```