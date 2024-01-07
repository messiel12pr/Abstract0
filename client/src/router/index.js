import { createRouter, createWebHistory } from 'vue-router'
import Editor from '../components/Editor.vue'

const CallbackComponent = () => import("../components/CallbackComponent.vue");

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/submit',
      name: 'submit',
      component: Editor
    },
    {
      path: '/callback',
      name: 'callback',
      component: CallbackComponent
    },
  ]
})

export default router