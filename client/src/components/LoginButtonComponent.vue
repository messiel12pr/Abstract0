<template>
    <button @click="handleLogin">Log In</button>
</template>
  
<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
const { loginWithRedirect } = useAuth0();

const handleLogin = () => {
    loginWithRedirect({
        appState: {
            target: '/callback'
        },
    });
};

</script>

<style scoped>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

button {
    padding: 9px 25px;
    background-color: #f1fa8c;
    border: none;
    border-radius: 50px;
    transition: background-color 0.3s ease 0s;
    font-size: larger;
}
</style>