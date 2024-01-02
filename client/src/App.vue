<template>
  <RouterView />
  <div>
    <!-- Other components or content -->
    <Editor />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<script>
import Editor from './components/Editor.vue';

export default {
  components: {
    Editor,
  },
  // Other component options...
};
</script>

