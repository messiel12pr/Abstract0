<template>
    <main>
        <div class="problem-set-container">
            <p>{{ problemSetData }}</p>
        </div>
    </main>
</template>
  
<script>
export default {
    props: ['problemSetData']
}   
</script> 

<style scoped>
.main {
    margin: 0;
    padding: 0;
}

.problem-set-container {
    background-color: #282c34;
    color: #e4e6eb;
    z-index: 1;
}
</style>