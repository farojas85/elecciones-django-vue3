<template>
    <div class="wrapper">
        <app-header></app-header>
        <menu-sidebar></menu-sidebar>
        <div class="content-wrapper">
            <router-view></router-view>
        </div>
        <Footer/>
        <Aside />
    </div>
</template>

<script>
import { onMounted } from 'vue'
import { addWindowClass, removeWindowClass, calculateWindowSize } from '../helpers'
import AppHeader from '../components/AppHeader.vue'
import MenuSidebar from '../components/MenuSidebar.vue'
import Footer from '../components/Footer.vue'
import Aside from '../components/Aside.vue'
export default {
    components:{
        AppHeader, MenuSidebar, Footer, Aside
    },
    setup() {
        onMounted(() => {
            removeWindowClass('register-page');
            removeWindowClass('login-page');
            removeWindowClass('hold-transition');
            addWindowClass('sidebar-mini')
            addWindowClass('layout-fixed')
            const screenSize = calculateWindowSize(window.innerWidth)
             
            if(['sm','xs'].includes(screenSize))
            {
                addWindowClass('sidebar-collapse')
            }
        })
    },
}
</script>