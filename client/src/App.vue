<template>
  <NavBarComponent />
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<script>
import NavBarComponent from './components/NavBarComponent.vue';

export default {
  components: {
    NavBarComponent,
  },
};
</script>