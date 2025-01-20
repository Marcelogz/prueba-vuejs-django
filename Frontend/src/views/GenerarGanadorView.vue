<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter()

const generarGanador = async () =>{
    try {
        const response = await axios.post('http://localhost:8000/api/generar-ganador/');
        alert('Ganador Generado!')
    } catch(error){
        console.error('Error al generar el ganador!', error)
    }
}
</script>

<template>
    <div>
        <h1>Generar Ganador</h1>
        <button @click="generarGanador">Generar Ganador</button>
    </div>
</template>

<style>
</style>