import axios from "axios"
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default function useAutenticacion() {
    const errors = ref([])

    const loginUsuario = async (data) => {
    }

    return {
        errors, loginUsuario
    }
}