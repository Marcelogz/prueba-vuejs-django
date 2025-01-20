<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import router from '../router';

const loginUsuario = async() => {
    try {
        await axios.post('http://localhost:8000/api/login/', {
            email: email.value,
            password: password.value
        });
        router.push('/generar-ganador')
    } catch (error){
        console.error('Error durante el proceso del Login', error)
    }
}
</script>

<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="loginUsuario">
            <input v-model="email" placeholder="Email" required />
            <input v-model="password" placeholder="Password" type="password" required />
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<style>
</style>