<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const email = ref('')
const nombre = ref('')
const apellido = ref('')
const router = useRouter

const registroUsuario = async () => {
    try{
        await axios.post('http://127.0.0.1:8000/usuarios/registro/',{
            email: email.value,
            nombre: nombre.value,
            apellido: apellido.value,
            password: 'password',
        });
        router.push('/verificacion-email')
    } catch (error){
        console.error('Error al registrar usuario', error)
    }
}
</script>

<template>
  <div>
    <form @submit.prevent="registroUsuario">
      <input v-model="email" placeholder="Email" required />
      <input v-model="nombre" placeholder="Nombre" required />
      <input v-model="apellido" placeholder="Apellido" required />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<style>
</style>