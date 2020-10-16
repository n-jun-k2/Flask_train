# FlaskからVue.jsを出力する手順

1. Pythonの環境のディレクトリ構成
    ```bash
    tmp/
    ├ public/ # 静的ファイル群
    │   ├ <Vue.jsプロジェクト>/
    │   │   ├ static
    │   │   │   ├ img
    │   │   │   ├ css
    │   │   │   └ js
    │   │   └ index.html
    │   ~
    └ app/ # pythonの各プロジェクト群
    ```
2. アプリケーションの設定を以下の設定を加える。
    ```python
    app = Flask(__name__, \
            root_path='../public', \
            static_folder='<Vue.jsプロジェクト名>/static', \
            template_folder='<Vue.jsプロジェクト名>')
    ```