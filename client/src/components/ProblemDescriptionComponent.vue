<template>
    <div id="container">
        <div v-if="htmlContent" v-html="htmlContent"></div>
        <div v-else>Loading...</div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            htmlContent: null,
        };
    },
    mounted() {
        // Replace 'description.html' with the path to your HTML file
        fetch('/path/to/description.html')
            .then(response => response.text())
            .then(html => {
                this.htmlContent = html;
            })
            .catch(error => {
                console.error('Error fetching HTML:', error);
            });
    },
};
</script>
  
<style scoped>
#container {
    overflow: hidden;
    margin: 0%;
    /* Remove default margin */
    background-color: #e4e6eb;
    width: 32%;
    /* Set the desired width of the editor */
    height: 70%;
    /* Set the desired height of the editor */
    margin: 1%;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 66%;
    border-radius: 1.5%;
}
</style>