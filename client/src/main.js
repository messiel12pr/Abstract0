import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Editor from './components/Editor.vue';
import ProblemDescriptionComponent from './components/ProblemDescriptionComponent.vue';
import NavBarComponent from './components/NavBarComponent.vue';

const app = createApp(App)

app.component('Editor', Editor);
app.component('ProblemDescriptionComponent', ProblemDescriptionComponent);
app.component('NavBarComponent', NavBarComponent);
app.use(router)
app.mount('#app')