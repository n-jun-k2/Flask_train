# Vue.js

Vue.jsは、クライアントであるブラウザでJavaScriptを使用しページを動的に生成するフレームワークです。

開発はNode.jsを利用します。
npmはNode.jsのパッケージマネージャーでNode.jsに付属されています。

# vue-cliとは
Vue.js向けのアプリケーション開発環境をセットアップする公式のコマンドラインツールです。

JavaScriptでアプリケーションを構築する場合，モジュール化，バンドラー／プリプロセッサによるビルド，JavaScriptの静的構文チェック（Lint⁠）⁠，単体テストやE2Eテストなどが必要になります。これらを満たした開発環境のセットアップは長期的なメンテナンスと開発の生産性を考えると必須とも言えますが，自分で一から用意するのはかなりの手間で，徒労感の伴う作業となるでしょう。この面倒なアプリケーション開発環境のセットアップを担ってくれるのがvue-cilと呼ばれるコマンドラインツールです。これによりすぐにVue.jsアプリケーションの開発に着手できます。

# プロジェクトの作成
```bash
$ vue create vue-application
# どれか選ぶ
Vue CLI v4.5.7
? Please pick a preset: (Use arrow keys)
❯ Default ([Vue 2] babel, eslint)
  Default (Vue 3 Preview) ([Vue 3] babel, eslint)
  Manually select features 
# あとは適当に選んでインストールを待つ。
...
```

# デフォルトプロジェクトの構成
```bash
<プロジェクトの作成で生成した名前のフォルダ>
├ node_modules/
│   └...  #npmでインストールされたpackageの格納先
├ public/
│   └...  #html,css,などのコードが格納される。
├ src/
│   └...  #vue.jsのコード類
├ .gitignore
├ babel.config.js
├ package-lock.json
├ package.json
└ README.md
```

> ``<noscript>``タグは使用するブラウザでJSスクリプトが動作出来ない状態の時にのみ表示されるタグ

# ``<div id="app">``タグについて
vue.jsでは``<div id=”app”>``に指定しているidをVueインスタンスの作成時に指定することでid=”app”以下の要素をすべてvue.jsの制御下に置くことができます。

# Single File Component
.vueはvue専用のファイルを表している拡張子で、中身は3つのパーツ(template, script, style)で構成されていることが確認できます。このファイルは単一ファイルコンポーネント(SFC : Single File Component)と呼ばれます。

```vue
<template>

</template>

<script>

</script>

<style>

</style>
```

# templateタグ
このタグはページの構成をマークアップ（HTML）で記述する。

# scriptタグ
このタグにはjavascriptを記述。

# styleタグ
このタグは、CSSを記述。


# Vueが表示するまでのフロー
Vue.jsはクライアントサイドのフレームワークであり、Vue.jsはブラウザ上で動作にページを作成しています。

1. サーバーがファイルの差分を検知
2. サーバーがビルドを行い、最小限のHTMLとJavascriptを作成
3. サーバーはページが更新された旨をブラウザに通知。
4. ブラウザはページを最横見しJavaScriptを使って動的にページを生成し、表示する。
