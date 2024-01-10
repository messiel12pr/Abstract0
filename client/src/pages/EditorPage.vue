<template>
    <NavBarComponent />
    <Editor />
    <ProblemDescriptionComponent />
</template>
  
<script>
import Editor from '../components/Editor.vue';
import ProblemDescriptionComponent from '../components/ProblemDescriptionComponent.vue';
import NavBarComponent from '../components/NavBarComponent.vue';

export default {
    components: {
        Editor,
        ProblemDescriptionComponent,
        NavBarComponent,
    },
};
</script>