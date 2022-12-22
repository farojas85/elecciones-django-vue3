<template>
    <div class="login-box">
        <router-view></router-view>
    </div>
</template>
<script>
import { onMounted } from 'vue'
import { addWindowClass, removeWindowClass } from '../helpers'
export default {
    setup() {
        onMounted(() => {
            removeWindowClass('sidebar-mini');
            removeWindowClass('layout-fixed');
            removeWindowClass('blank-page');
            addWindowClass('login-page')
        })
    },
}
</script>