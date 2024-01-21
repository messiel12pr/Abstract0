<template>
    <main>
        <div class="problem-set-container">
            <ul>
                <li v-for="(i) in problemSetData">
                    <h3>{{ i[0] }}</h3>
                    <ul>
                        <li v-for="(value, key) in i[1]">
                            <div class="problem">{{ key }}</div>
                        </li>
                    </ul>
                    <br>
                </li>
            </ul>
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
    background-color: #e4e6eb;
    color: #282c34;
    padding: 20px 180px;
    border-radius: 4px;
    width: 800px;
    height: 580px;
    overflow-y: scroll;
}

ul,
ol {
    list-style: none;
    padding: 0;
    margin: 0;
}

h3 {
    line-height: 2;
    border-bottom: 1px solid #282c34;
    text-align: center;
}

.problem {
    border: solid;
    border-color: #282c34;
    border-radius: 6px;
    border-width: 1.5px;

    margin-bottom: 10px;
    padding: 10px;
    text-align: center;
    transition: 1s;
}

.problem:hover {
    background-color: #282c34;
    color: #e4e6eb;
    transition: .5s;
    cursor: pointer;
}
</style>