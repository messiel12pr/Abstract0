import { createRouter, createWebHistory } from 'vue-router'
import EditorPage from '../pages/EditorPage.vue'
import EditorComponent from '../components/Editor.vue'
import CallbackComponent from '../components/CallbackComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: EditorPage
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