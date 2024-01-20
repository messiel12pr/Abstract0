<template>
    <div id="container">
        <div id="description" v-if="htmlContent" v-html="htmlContent"></div>
        <div v-else>Loading...</div>
    </div>
</template>
  
<script>
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const htmlContent = ref();

        onMounted(() => {
            fetch('../problem_description.html')
                .then(response => response.text())
                .then(html => {
                    htmlContent.value = html;
                })
                .catch(error => {
                    console.error('Error fetching HTML:', error);
                });
        });

        return {
            htmlContent,
        }
    }
};
</script>
  
<style scoped>
#container {
    overflow: hidden;
    background-color: #e4e6eb;
    border-radius: 0.5em;
    overflow-y: scroll;
}

#description {
    margin: 6%;
}
</style>