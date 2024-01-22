<template>
    <body>
        <div class="container">
            <main class="grid">
                <img src="../assets/graph.png" alt="graph">
                <div class="welcome">
                    <h2><img src="../assets/logo.svg" alt="logo" class="logo">ABSTRACT0</h2>
                    <p>Welcome to Abstract0, a dynamic learning platform with a primary focus on Data Structures and
                        Algorithms.</p>
                    <p>Our dedicated mission is to empower students to excel in their tests and coding interviews!</p>
                </div>
                <h2>FEATURES</h2>
                <div class="card">
                    <h3><a href="/editor">Online Code Editor</a></h3>
                    <p>Access our robust online code editor, powered by Ace and Judge0, supporting languages such as C++,
                        Python, and Java.</p>
                    <p>Run your code effortlessly without the hassle of setting up a coding environment!</p>
                </div>
                <div class="card">
                    <h3><a href="/problems">Coding Problems</a></h3>
                    <p>Solidify your understanding through interactive hands-on practice sessions.</p>
                    <p>Challenging problems await, designed to enhance your problem-solving skills and reinforce key
                        concepts.</p>
                </div>
                <div class="card">
                    <h3><a href="#">Resources</a></h3>
                    <p>Explore our curated collection of programming resources, spanning video tutorials, books, courses,
                        and repositories.</p>
                    <p>Empower your learning journey with diverse and valuable educational materials.</p>
                </div>
            </main>

        </div>
    </body>
</template>

<script>

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;500;600;800&family=VT323&display=swap');

body {
    margin: 0;
    padding: 0;
}

.logo {
    max-height: 37px;
    position: absolute;
    margin-left: 35px;
}

.container {
    font-family: "Poppins";
    margin: 0 auto;
    padding: 1% 3%;
    border-radius: 0.5em;
}

.grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 30px;
}

main {
    max-width: 1200px;
    margin: 60px auto;
    padding: 20px;
}

main img {
    grid-column: span 6;
    width: 100%;
    border-radius: 6px;
}

main .welcome {
    grid-column: 8 / span 5;
    font-size: 1.3em;
    color: #e4e6eb;
    padding: 10px 20px;
    border-radius: 6px;
    margin-top: 20%;
}

main .welcome h2 {
    color: #F1FA8C;
    width: 350px;
    position: relative;
}

.grid h2 {
    color: #F1FA8C;
}

main>h2 {
    grid-column: span 12;
    text-align: center;
    font-size: 1.5em;
    color: #e4e6eb;
    padding-top: 20px;
}

main .card {
    grid-column: span 4;
    background: #e4e6eb;
    padding: 10px 20px;
    border-radius: 6px;
    box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.05);
}

main .card h3 {
    text-align: center;
}

a {
    background-color: transparent;
    text-decoration: none;
    color: #BD93F9;
}

@media screen and (max-width: 960px) {
    main img {
        grid-column: 2 / span 10;
    }

    main .welcome {
        grid-column: 3 / span 8;
        text-align: center;
    }

    main .card {
        grid-column: 3 / span 8;
    }

    main {
        justify-items: center;
    }
}
</style>