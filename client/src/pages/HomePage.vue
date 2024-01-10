<template>
    <div>
        <div class="container">
            <div class="box">Box</div>
            <div class="box">Box</div>
            <div class="box">Box</div>
            <div class="box">Box</div>
            <div class="rectangle">Rectangle</div>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
body {
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.container {
    flex: 1;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    padding: 20px;
}

.box {
    width: 150px;
    height: 150px;
    background-color: #e4e6eb;
    border-radius: 10px;
    margin: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #282A36;
    font-size: 1.2em;
}

.rectangle {
    width: 300px;
    height: 150px;
    background-color: #F1FA8C;
    border-radius: 10px;
    margin: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #282A36;
    font-size: 1.2em;
}
</style>