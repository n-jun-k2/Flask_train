<template>
  <div id="app">
    <h1>{{hello}}</h1>
    <h2>{{world}}</h2>
  </div>
</template>

<script>
// export文でバインドを行う
// バインド対象は変数、関数、クラス
// exportは2種類存在する。名前付きとdefaultです。

// 名前付きは、その名前で参照しますが、
// defaultは、import文で名前を指定します。 
// import m from '<export defaultが書かれたjsファイル名>'

export default {
  name: 'app',
  data() {
    return {
      hello: "こんにちは",
      world: "世界"
    }
  }
}
</script>

