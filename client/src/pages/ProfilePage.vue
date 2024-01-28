<template>
    <body>
        <NavBarComponent />

        <div class="card-container">
            <div class="profile__header">
                <img :src="user.picture" alt="Profile" class="profile__avatar" />
                <div class="profile__headline">
                    <h2 class="profile__title">{{ user.name }}</h2>
                    <h3 class="profile__info">Problems solved: </h3>
                    <h3 class="profile__info">Contact: <a href="mailto: joel.gonzalez35@upr.edu">email</a></h3>
                </div>
            </div>
        </div>
    </body>
</template>
  
<script setup>
import { useAuth0 } from "@auth0/auth0-vue";
const { user } = useAuth0();
</script>

<script>
import NavBarComponent from '../components/NavBarComponent.vue';

export default {
    components: {
        NavBarComponent,
    },
};
</script>

<style scoped>
body {
    font-family: "Arial", sans-serif;
    line-height: 1.6;
    margin: 20px;
}

.card-container {
    display: flex;
    justify-content: center;
    height: max-content;
    padding: 20px;
    margin-top: 10px;
    box-sizing: border-box;
    background-color: #282c34;
    color: #e4e6eb;
    border-radius: 8px;
}

.profile__avatar {
    border: none;
    border-radius: 300px;
    max-width: 100%;
}

.profile__headline {
    text-align: center;
}

a {
    text-decoration: none;
    color: #BD93F9;
}

.profile__title {
    padding: 20px;
}

.profile__info {
    border-top: solid;
    border-color: #F1FA8C;
    text-align: left;
    line-height: 100px;
}
</style>