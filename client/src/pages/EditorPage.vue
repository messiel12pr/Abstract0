<template>
    <Editor />
    <ProblemDescriptionComponent />
</template>
  
<script>
import Editor from '../components/Editor.vue';
import ProblemDescriptionComponent from '../components/ProblemDescriptionComponent.vue';

export default {
    components: {
        Editor,
        ProblemDescriptionComponent,
    },
};
</script>