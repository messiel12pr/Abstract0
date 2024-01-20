<template>
    <div>
        <NavBarComponent />
        <div class="editor-container">
            <Editor />
        </div>
    </div>
</template>
  
<script>
import Editor from '../components/Editor.vue';
import NavBarComponent from '../components/NavBarComponent.vue';

export default {
    components: {
        Editor,
        NavBarComponent,
    },
};
</script>

<style>
.editor-container {
    margin-top: 20px;
}
</style>