import { createRouter, createWebHistory } from 'vue-router'

import LayoutLogin from '../layouts/AppLayoutLogin.vue'
import LayoutDefault from '../layouts/AppLayoutDefault.vue'

import Login from '../pages/auth/Login.vue'
import Home from '../pages/Home.vue'

const routes = [
    {
        path: '/', name: 'Login', component: Login,
        meta: { layout: LayoutLogin }
    },
    {
        path: '/home', name: 'Home', component: Home,
        meta: { layout: LayoutDefault }
    }
]

export default createRouter({
    history: createWebHistory(),
    routes
})