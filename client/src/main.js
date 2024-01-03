import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Editor from './components/Editor.vue';
import ProblemDescriptionComponent from './components/ProblemDescriptionComponent.vue';

const app = createApp(App)

app.component('Editor', Editor);
app.component('ProblemDescriptionComponent', ProblemDescriptionComponent);
app.use(router)
app.mount('#app')