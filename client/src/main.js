import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Editor from './components/Editor.vue';
import 'bootstrap/dist/css/bootstrap.css'
import './assets/main.css'

const app = createApp(App)

app.component('Editor', Editor);
app.use(router)
app.mount('#app')