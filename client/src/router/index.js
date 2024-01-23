import { createRouter, createWebHistory } from 'vue-router';
import Editor from '../pages/EditorPage.vue';
import EditorComponent from '../components/Editor.vue';
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
      path: '/problems',
      name: 'problems',
      component: Problems
    },
    {
      path: '/problems/:id',
      name: 'problem',
      component: Editor,
      props: true
    },
    {
      path: '/submit',
      name: 'submit',
      component: EditorComponent
    },
    {
      path: '/callback',
      name: 'callback',
      component: Home
    },
  ]
})

export default router