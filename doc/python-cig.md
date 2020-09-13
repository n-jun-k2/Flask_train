# PythonでCGI
CGI（Common Gateway Interface）Webアプリケーション開発のメモ

## 仕組み
WebサーバーがCGIプログラム（スクリプト）を実行し、そのプログラムの標準出力の結果をHTTP通信の応答として返す。

Pythonの標準モジュールに```http.server```というCGIプログラムを実行可能なWebサーバーがあります。

## 使用方法

### サーバーから返すスクリプト作成
標準出力を行うPythonコードを作成します。<br>
#### ※```#!```はShebang(シバン)Unix系システムにおいて、ファイルに書かれたプログラム分をどうやって実行するかを指定。　この記載ないとCGIから呼び出されない。
```hello.py
#!/usr/bin/env python3 
print("200 ok")
print("Content-Type: text/plain")
print("")
print("Hello CGI")
```

```cgi-bin```というフォルダ内にスクリプトを格納し実行権限等を付与する。

```
chmod u+x cgi-bin/hello.py
```
ブラウザから```http://localhost:5000/cgi-bin/hello.py```へ接続して
```
Hello CGI
```
と表示される。