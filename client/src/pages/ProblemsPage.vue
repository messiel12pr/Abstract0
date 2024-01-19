<template>
    <NavBarComponent />
    <!-- 
    <main class="grid">
        <div class="container mx-auto mt-4">
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 25rem">
                        <img src="https://oklahoma-cannabis-company.com/wp-content/uploads/2021/07/Coming-Soon-Photo-2048x2048.jpeg"
                            class="card-img-top" width="300" height="400" alt="..." />
                        <div class="card-body">
                            <h5 class="card-title">Data Structures and Algorithms</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                            <p class="card-text">Learn the basics of Data Structures</p>
                            <a @click="activateComponent(dsProblemSetData)" class="btn mr-2">Start</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container mx-auto mt-4">
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 25rem">
                        <img src="https://oklahoma-cannabis-company.com/wp-content/uploads/2021/07/Coming-Soon-Photo-2048x2048.jpeg"
                            class="card-img-top" width="300" height="400" alt="..." />
                        <div class="card-body">
                            <h5 class="card-title">Lorem ipsum dolor sit amet</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                            <p class="card-text">Netus et malesuada fames ac turpis</p>
                            <a @click="activateComponent(dsProblemSetData)" class="btn mr-2">Start</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container mx-auto mt-4">
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 25rem">
                        <img src="https://oklahoma-cannabis-company.com/wp-content/uploads/2021/07/Coming-Soon-Photo-2048x2048.jpeg"
                            class="card-img-top" width="300" height="400" alt="..." />
                        <div class="card-body">
                            <h5 class="card-title">Lorem ipsum dolor sit amet</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                            <p class="card-text">Netus et malesuada fames ac turpis</p>
                            <a @click="activateComponent(dsProblemSetData)" class="btn mr-2">Start</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container mx-auto mt-4">
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 25rem">
                        <img src="https://oklahoma-cannabis-company.com/wp-content/uploads/2021/07/Coming-Soon-Photo-2048x2048.jpeg"
                            class="card-img-top" width="300" height="400" alt="..." />
                        <div class="card-body">
                            <h5 class="card-title">Lorem ipsum dolor sit amet</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Beginner</h6>
                            <p class="card-text">Netus et malesuada fames ac turpis</p>
                            <a @click="activateComponent(dsProblemSetData)" class="btn mr-2">Start</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="problem-selection-container" v-if="isActivated">
            <button @click="deactivateComponent()" type="button" class="btn-close" aria-label="Close"></button>
            <ProblemSetComponent v-bind:problemSetData="data" />
        </div>
    </main>
    -->
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
.grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    position: absolute;
    width: 100%;
    height: 100%;
}

main {
    position: absolute;
    top: 9%;
    left: 0.2%;
}

.container {
    grid-column: span 3;
}

.problem-selection-container {
    background-color: #e4e6eb;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 2%;
    border-radius: 1.5%;
    overflow-y: scroll;
    grid-column: span 12;
}

.btn-close {
    background-color: red;
}

.card {
    background: #282c34;
    color: #edf0f1;
}

.btn {
    color: #282a36;
    background-color: #f1fa8c;
    width: 25%;
}
</style>