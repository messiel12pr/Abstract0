import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'

import { createAuth0 } from '@auth0/auth0-vue'
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

app
  .use(router)
  .use(
    createAuth0({
      domain: import.meta.env.VITE_AUTH0_DOMAIN,
      clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
      authorizationParams: {
        redirect_uri: import.meta.env.VITE_AUTH0_CALLBACK_URL,
      },
    })
  )
app.mount('#app')