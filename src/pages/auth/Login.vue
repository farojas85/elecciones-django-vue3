<template>
    <div class="card card-outline card-primary">
        <div class="card-header text-center">
            <a href="/" class="h1"><b>Sufragio</b>ADP</a>
        </div>
        <div class="card-body">
            <p class="login-box-msg">Iniciar Sesi&oacute;n</p>
            <form action="" @submit.prevent="autenticar">
                <div class="form-group row">
                    <div class="col-md-12">
                        <div class="input-group">
                            <input type="text" class="form-control" placeholder="Nombre de Usuario"
                                v-model="usuario.name"
                                :class="{ 'is-invalid' : errors.name }"/>
                            <div class="input-group-append">
                                <div class="input-group-text">
                                    <span class="fas fa-user"></span>
                                </div>
                            </div>
                        </div>
                        <small class="text-danger" v-for="error in errors.name"
                            :key="error">{{ error }}</small>
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-md-12">
                        <div class="input-group">
                            <input type="password" class="form-control" placeholder="Contraseña"
                                v-model="usuario.password"
                                :class="{ 'is-invalid' : errors.password }" />
                            <div class="input-group-append">
                                <div class="input-group-text">
                                <span class="fas fa-lock"></span>
                                </div>
                            </div>
                        </div>
                        <small class="text-danger" v-for="error in errors.password"
                            :key="error">{{ error }}</small>
                    </div>
                </div>
                <div class="row">
                    <div class="col-8">
                        <div class="icheck-primary">
                        <input type="checkbox" id="remember">
                        <label for="remember">
                            Recordarme
                        </label>
                        </div>
                    </div>
                    <div class="col-4">
                        <button type="submit" class="btn btn-primary btn-block">
                            Acceder
                        </button>
                    </div>                    
                </div>
            </form>
            <div class="social-auth-links text-center mt-2 mb-3">
                <a href="#" class="btn btn-block btn-primary">
                    <i class="fab fa-facebook mr-2"></i> Acceder con Facebook
                </a>
                <a href="#" class="btn btn-block btn-danger">
                    <i class="fab fa-google mr-2"></i> Acceder con Google
                </a>
                <p class="mb-1">
                    <a href="forgot-password.html">Olvid&eacute; mi contrase&ntilde;a</a>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive } from 'vue'
import useAutenticacion from '../../composables/autenticacion'
export default {
    setup() {

        const {errors, loginUsuario } = useAutenticacion()

        const usuario = reactive({
            name: '',
            password: ''
        })


        const autenticar = async() => {
            await loginUsuario(...usuario)
        }

        return {
            errors, usuario,
            autenticar
        }
    },
}
</script>