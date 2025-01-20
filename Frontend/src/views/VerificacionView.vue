<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute()

const verificarCorreo = async() => {
    const usuarioId = route.params.id
    try {
        await axios.put(`http://localhost:8000/api/verificacion-email/${usuarioId}/`)
        alert('Correo verificado correctamente!')
    } catch (error){
        console.error('Error al verificar el correo', error)
    }
}
</script>

<template>
    <div>
        <h1>Verifica tu correo</h1>
        <button @click="verificarCorreo">Verificar</button>
    </div>
</template>

<style>
</style>