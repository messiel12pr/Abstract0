import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Editor from './components/Editor.vue';

const app = createApp(App)

app.component('Editor', Editor);
app.use(router)
app.mount('#app')

// Save editor content to local storage before page unload
window.addEventListener('beforeunload', () => {
    const editorContent = vueApp.$refs.editor.editor.getValue();
    localStorage.setItem('editorContent', editorContent);
  });
