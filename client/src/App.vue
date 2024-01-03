<template>
  <RouterView />
  <div>
    <!-- NavBarComponent -->
    <Editor />
    <ProblemDescriptionComponent />
    <!-- ProblemDescriptionComponent -->
    <!-- SubmissionResultComponent -->
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<script>
import Editor from './components/Editor.vue';
import ProblemDescriptionComponent from './components/ProblemDescriptionComponent.vue';

export default {
  components: {
    Editor,
    ProblemDescriptionComponent,
  },
  // Other component options...
};
</script>