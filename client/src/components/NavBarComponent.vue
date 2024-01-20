<template>
    <header>
        <a href="/home"><img src="../assets/logo.svg" alt="logo" style="width: 55px; height: 55px; margin-right: 2rem"></a>

        <nav>
            <ul class="nav__links">
                <li><a href="/editor">Editor</a></li>
                <li><a href="/problems">Problems</a></li>
                <li><a href="#">Resources</a></li>
            </ul>
        </nav>

        <div class="buttons">
            <loginButton />
            <logoutButton />
        </div>
    </header>
</template>
  
<script>
import loginButton from '../components/LoginButtonComponent.vue';
import logoutButton from '../components/LogoutButtonComponent.vue';

export default {
    components: {
        loginButton,
        logoutButton
    },
};
</script>
  
<style scoped>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 5%;
    background-color: #282c34;
    border-radius: 0.5em;
}

.nav__links a {
    font-family: "Montserrat", sans-serif;
    font-weight: 500;
    color: #edf0f1;
    text-decoration: none;
}

.nav__links {
    list-style: none;
    display: flex;
}

.nav__links li {
    padding: 0px 20px;
}

.nav__links li a {
    transition: color 0.3s ease 0s;
    font-size: larger;
}

.nav__links li a:hover {
    color: #f1fa8c;
}

.buttons {
    display: flex;
    gap: 3rem;
    box-sizing: border-box;
}

@media only screen and (max-width: 800px) {

    .nav__links {
        display: none;
    }
}
</style>