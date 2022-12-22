import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve,dirname } from 'path'
import { fileURLToPath } from 'url'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      template:{
        transformAssetUrls:{
          base: null,
          includeAbsolute: false,
        }
      }
    }),
  ],
  resolve:{
    alias:{
      '@': resolve(__dirname, './src')
    }
  },
  build: {
    chunkSizeWarningLimit: 2000,
  },
})
