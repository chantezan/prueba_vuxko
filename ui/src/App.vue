<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcomeee tasdasdo Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import SeeBot from './components/SeeBot.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    SeeBot
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
