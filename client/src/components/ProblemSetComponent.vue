<template>
    <main>
        <div class="problem-set-container">
            <div class="title">
                <div></div>
                <hr>
            </div>
            <ul>
                <li v-for="(i) in problemSetData">
                    <h3>{{ i[0] }}</h3>
                    <ul>
                        <li v-for="(value, key) in i[1]">
                            <a v-if="value != '0'" :href="`/problems/${value}`">
                                <div class="problem">{{ key }}</div>
                            </a>

                            <a v-else>
                                <div class="problem">{{ key }}</div>
                            </a>
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


.problem-set-container>ul {
    padding: 20px 180px;
}

.problem-set-container {
    background-color: #282c34;
    color: #e4e6eb;
    border-radius: 10px;
    width: 800px;
    height: 580px;
    overflow-y: scroll;

    border: solid;
    border-color: #ABB2BF;
    border-width: 1px;
}

.title {
    top: 0;
    background-color: #ABB2BF;
    position: sticky;
    text-align: center;
    color: #282c34;
}

.title>hr {
    margin-top: 0px;
    height: 0px;
}

.title>div {
    height: 25px;
}

ul,
ol {
    list-style: none;
    padding: 0;
    margin: 0;
}

a {
    outline: none;
    text-decoration: none;
    color: #e4e6eb;
}

h3 {
    line-height: 2.5;
    text-align: center;
}

.problem {
    border: solid;
    border-color: #ABB2BF;
    border-radius: 10px;
    border-width: 1.5px;

    margin-bottom: 10px;
    padding: 10px;
    text-align: center;
    transition: 1s;
}
</style>