<template>
  <RouterView />
  <div>
    <NavBarComponent />
    <Editor />
    <ProblemDescriptionComponent />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<script>
/*
    <Editor />
    <ProblemDescriptionComponent />
*/


import Editor from './components/Editor.vue';
import ProblemDescriptionComponent from './components/ProblemDescriptionComponent.vue';
import NavBarComponent from './components/NavBarComponent.vue';

export default {
  components: {
    Editor,
    ProblemDescriptionComponent,
    NavBarComponent,
  },
  // Other component options...
};
</script>