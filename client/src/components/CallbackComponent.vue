<template>
    <div class="page-layout">
        <NavBar />
        <div class="page-layout__content">
            <slot />
        </div>
    </div>
</template>
  
<script>
import NavBar from "./NavBarComponent.vue";

export default {
    components: {
        NavBar,
    },
};
</script>