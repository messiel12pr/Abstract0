<template>
    <NavBarComponent />

    <PageLayout>
        <div class="content-layout">
            <h1 id="page-title" class="content__title">Profile Page</h1>
            <div class="content__body">
                <div class="profile-grid">
                    <div class="profile__header">
                        <img :src="user.picture" alt="Profile" class="profile__avatar" />
                        <div class="profile__headline">
                            <h2 class="profile__title">{{ user.name }}</h2>
                            <span class="profile__description">{{ user.email }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </PageLayout>
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

<style>
body {
    font-family: "Arial", sans-serif;
    line-height: 1.6;
    margin: 20px;
}
</style>