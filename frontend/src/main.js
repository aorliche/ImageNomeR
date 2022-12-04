import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

createApp(App)
  .use(createPinia())
  .mount('#app')
