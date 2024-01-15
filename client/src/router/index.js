import { createRouter, createWebHistory } from 'vue-router';
import Editor from '../pages/EditorPage.vue';
import EditorComponent from '../components/Editor.vue';
import CallbackComponent from '../components/CallbackComponent.vue';
import Home from '../pages/HomePage.vue';
import Problems from '../pages/ProblemsPage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '',
      component: Home
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/editor',
      name: 'editor',
      component: Editor    
    },
    {
      path: '/problems',
      name: 'problems',
      component: Problems
    },
    {
      path: '/submit',
      name: 'submit',
      component: EditorComponent
    },
    {
      path: '/callback',
      name: 'callback',
      component: CallbackComponent
    },
  ]
})

export default router