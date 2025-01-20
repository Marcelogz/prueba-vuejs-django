import { createRouter } from 'vue-router'
import { createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import RegistroView from '../views/RegistroView.vue'
import VerificacionView from '../views/VerificacionView.vue'
import LoginView from '../views/LoginView.vue'
import GenerarGanadorView from '../views/GenerarGanadorView.vue'

const routes = [
        {
            path: '/',
            name: 'Registro',
            component: RegistroView,
        },
        {
            path: '/verificacion-email',
            name: 'Verificacion',
            component: VerificacionView,
        },
        {
            path: '/login',
            name: 'Login',
            component: LoginView,
        },
        {
            path: '/generar-ganador',
            name: 'GenerarGanador',
            component: GenerarGanadorView,
            meta: {requiresAuth: true},
        }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

export default router