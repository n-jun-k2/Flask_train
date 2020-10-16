# Vue.jsでプロジェクトを作成する際の手順書

1. vue.jsのプロジェクトを生成
    ```bash
    $ vue create <Vue.jsプロジェクト名>
    ```
1. vue.jsのビルド成果物の出力先を変更するpackage.jsonの以下の項目を変更する。
    ```json
    "scripts": {
        "serve": "vue-cli-service serve",
        "build": "vue-cli-service build --dest ../dist/<プロジェクト名>",
        "lint": "vue-cli-service lint"
      },
    ```
1. ビルド後、静的ファイルたちを``static``フォルダに入れる用にする為,Vue.jsプロジェクトディレクトリ直下に``vue.config.js``を作成。
    ```javascript
    module.exports = {
        assetsDir: 'static',
    }
    ```
1. Vue.jsプロジェクトディレクトリの``public``フォルダにある静的ファイルを``static``フォルダに格納するようにする。
    ```bash
    vue-app/        # Vue.jsのプロジェクト
    ├ public/
    │    ├ static/ #静的ファイルを入れる場所
    │    │   ├ img
    │    │   ├ js
    │    │   └ css
    │    └ index.html 
    ```