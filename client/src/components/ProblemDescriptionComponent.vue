<template>
    <div id="container">
        <div id="description" v-if="htmlContent" v-html="htmlContent"></div>
        <div v-else>Loading...</div>
    </div>
</template>
  
<script>
import { ref, onBeforeMount, onMounted } from 'vue';
import { useRoute } from "vue-router";
import axios from 'axios';

export default {
    setup() {
        const htmlContent = ref();
        const problemLocation = ref();
        const route = useRoute();

        onMounted(async () => {
            await getProblemDescriptionLocation();

            fetch(problemLocation.value)
                .then(response => response.text())
                .then(html => {
                    htmlContent.value = html;
                })
                .catch(error => {
                    console.error('Error fetching HTML:', error);
                });
        });

        const getProblemDescriptionLocation = async () => {
            try {
                const path = 'http://localhost:5001/problems/' + route.params.id;

                await axios.get(path)
                    .then((res) => {
                        problemLocation.value = res["data"];
                    })
                    .catch((error) => {
                        console.error(error.data);
                    });
            }
            catch (error) {
                console.log(error.message)
            }
        }

        return {
            htmlContent,
            problemLocation,
        }
    },

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