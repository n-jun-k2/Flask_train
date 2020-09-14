# Error Memo

## mysqlコンテナが立ち上がらない場合
``docker-compose logs <コンテナ名>``でログを確認し対応する。

## docker-entrypoint-initdb内のファイルでエラーが出ている場合
dockerのvolumeを削除しdockerのコンテナを立ち上げなおす。

## mysqlの日本語対応には以下のようにする
1. mysqlの日本語入力対応として```my.cnf```に以下の項目をそれぞれ```utf8mb4```に設定し再起動する。
    ```
    [client]
    default-character-set=utf8mb4

    [mysql]
    default-character-set=utf8mb4

    [mysqldump]
    default-character-set=utf8mb4

    [mysqld]
    character-set-server=utf8mb4
    ```
1. sqlalchemyのログインURLのcharsetを指定する
    ```
    engine = create_engine('mysql://dev:dev@mysql/sample_db?charset=utf8mb4')
    ```