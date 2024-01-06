<template>
    <div id="container">
        <header>
            <a class="logo" href="/">
                <!-- Add inline styles to the img tag to adjust the size -->
                <img src="../assets/logo.svg" alt="logo" style="width: 50px; height: 50px;">
            </a>

            <nav>
                <ul class="nav__links">
                    <li><a href="#">Roadmap</a></li>
                    <li><a href="#">Problems</a></li>
                    <li><a href="#">Resources</a></li>
                </ul>
            </nav>
            <loginButton class="cta" />
            <p class="menu cta">Menu</p>
        </header>
    </div>
</template>
  
<script>
import loginButton from '../components/LoginButtonComponent.vue';

export default {
    components: {
        loginButton,
    },
};
</script>
  
<style scoped>
#container {
    position: absolute;
    width: 98%;
    height: 10%;
    top: 2%;
    right: 1%;
    bottom: 0%;
    white-space: nowrap;
    overflow: hidden;
}

a {
    background-color: transparent
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

header {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0.5%;
    background-color: #282c34;
    border-radius: 10px;
}

.logo {
    cursor: pointer;
}

.nav__links a,
.cta,
.overlay__content a {
    font-family: sans-serif;
    font-weight: 500;
    font-size: 1.2em;
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
}

.nav__links li a:hover {
    color: #f1fa8c;
}

.cta {
    color: #282A36;
    padding: 9px 25px;
    background-color: #f1fa8c;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: background-color 0.3s ease 0s;
}

/*
.cta:hover {
    background-color: #f1fa8c;
}
*/

.menu {
    display: none;
}
</style>