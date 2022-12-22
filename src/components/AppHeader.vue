<template>
    <nav id="main-header" class="main-header navbar navbar-expand navbar-white navbar-light" >
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" data-widget="pushmenu" href="#" role="button">
                    <i class="fas fa-bars"></i>
                </a>
            </li>
            <li class="nav-item d-none d-sm-inline-block">
                <router-link to="/home" class="nav-link">
                    Home
                </router-link>
            </li>
            <li class="nav-item d-none d-sm-inline-block">
                <router-link to="" class="nav-link">
                    Contacto
                </router-link>
            </li>
        </ul>

        <ul class="navbar-nav ml-auto">
            <!-- <messages-dropdown></messages-dropdown>
            <notifications-dropdown></notifications-dropdown>
            <languages-dropdown></languages-dropdown>
            <user-dropdown></user-dropdown> -->
            <li class="nav-item">
                <a class="nav-link" data-widget="control-sidebar" data-controlsidebar-slide="true" href="#" role="button">
                <i class="fas fa-th-large"></i>
                </a>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    setup() {
        
    },
}
</script>