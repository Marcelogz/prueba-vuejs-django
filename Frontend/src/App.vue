<script setup>
import HelloWorld from './components/HelloWorld.vue'
import ComponenteX from './components/ComponenteX.vue'
import Home from './views/Home.vue'

const numero = []
</script>


<template>
  <nav>
    <router-link to="/">Registro</router-link><br>
    <router-link to="/verificacion-email">Verificacion</router-link><br>
    <router-link to="/login">Login</router-link><br>
    <router-link to="/generar-ganador">Generar Ganador</router-link>
  </nav>
  <router-view></router-view>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
