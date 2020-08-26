# Error Memo

## mysqlコンテナが立ち上がらない場合
``docker-compose logs <コンテナ名>``でログを確認し対応する。

## docker-entrypoint-initdb内のファイルでエラーが出ている場合
dockerのvolumeを削除しdockerのコンテナを立ち上げなおす。