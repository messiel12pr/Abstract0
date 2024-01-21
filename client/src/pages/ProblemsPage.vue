<template>
    <body>
        <NavBarComponent />

        <div class="problem-selection-container" v-if="isActivated">
            <button @click="deactivateComponent()" type="button" class="btn-close" aria-label="Close"></button>
            <ProblemSetComponent v-bind:problemSetData="data" />
        </div>

        <div class="cards">
            <div @click="activateComponent(dsProblemSetData)" class="card">
                <img class="card__image" src="../assets/images/Binary_tree.png" alt="">
                <div class="card__content">
                    <div class="card-body">
                        <h5 class="card-title">Data Structures and Algorithms</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                        <p class="card-text">Learn basic Data Structures</p>
                    </div>
                </div>
            </div>

            <div @click="activateComponent(dsProblemSetData)" class="card">
                <img class="card__image" src="../assets/images/OOP.png" alt="">
                <div class="card__content">
                    <div class="card-body">
                        <h5 class="card-title">Object Oriented Programming</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                        <p class="card-text">Learn the basics of OOP</p>
                    </div>
                </div>
            </div>

            <div @click="activateComponent(dsProblemSetData)" class="card">
                <img class="card__image" src="../assets/images/Sorting.png" alt="">
                <div class="card__content">
                    <div class="card-body">
                        <h5 class="card-title">Algorithms</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                        <p class="card-text">Learn basic Algorithms</p>
                    </div>
                </div>
            </div>
        </div>

    </body>
</template>
  
<script>
import NavBarComponent from "../components/NavBarComponent.vue";
import ProblemSetComponent from "../components/ProblemSetComponent.vue";
import { ref } from "vue";

export default {
    setup() {
        const isActivated = ref(false);
        const data = ref();

        const listHm = {
            "Implement add method": "1",
            "Implement remove method": "2",
        };

        const stackHm = {
            "Implement push method": "3",
            "Implement pop method": "4",
        };

        const queueHm = {
            "Implement enqueue method": "5",
            "Implement dequeue method": "6",
        };

        const dsProblemSetData = [
            ["Li, reactive, watch, onMounted, onBeforeUnmountst", listHm],
            ["Stack", stackHm],
            ["Queue", queueHm],
        ];

        const activateComponent = (problemSet) => {
            data.value = problemSet;
            isActivated.value = true;
        };

        const deactivateComponent = () => {
            data.value = null;
            isActivated.value = false;
        };

        return {
            isActivated,
            data,
            dsProblemSetData,
            activateComponent,
            deactivateComponent,
        };
    },
    components: {
        NavBarComponent,
        ProblemSetComponent,
    },
};
</script>
  
<style scoped>
body {
    font-family: "Arial", sans-serif;
    line-height: 1.6;
    margin: 20px;
}

.problem-selection-container {
    position: absolute;
    top: 50%;
    bottom: 50%;
    z-index: 1;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    grid-auto-rows: auto;
    gap: 20px;
    font-family: sans-serif;
    padding-top: 100px;
}

.cards * {
    box-sizing: border-box;
}

.card {
    background-color: #282c34;
    width: max-content;
    margin: 0 auto;
    transition: 1s;
}

.card:hover {
    cursor: pointer;
    transform: scale(1.08);
    transition: .5s;
    box-shadow: 18px 18px 50px #131313,
        -18px -18px 50px #1d1d1d;
}

.card__content,
.card__info,
.card-body {
    background-color: #282c34;
    color: #edf0f1;
    padding: 15px;
}

.card__info {
    margin: 0 auto;
    width: 30%;
}

.card__image {
    height: 450px;
    object-fit: fill;
}

.btn {
    color: #282a36;
    background-color: #f1fa8c;
    width: 100%;
}

.btn-close {
    background-color: red;
}
</style>