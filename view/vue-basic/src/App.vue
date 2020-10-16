<template>
  <div id="app">
    <h1>{{hello}}</h1>
    <h2>{{world}}</h2>
  </div>
</template>

<script>
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

