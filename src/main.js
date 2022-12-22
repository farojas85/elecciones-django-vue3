import { createApp } from 'vue'
import App from './App.vue'
import Router from './router'
import './style.css'
// import './bootstrap'

const app = createApp(App)
app.use(Router)
app.mount('#app')
