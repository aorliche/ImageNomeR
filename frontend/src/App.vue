<template>
    <SidePanel/>
    <MainPanel/>
</template>

<script>
import SidePanel from './components/SidePanel.vue'
import MainPanel from './components/MainPanel.vue'

export default {
    name: 'App',
    components: {
        SidePanel,
        MainPanel
    }
}
</script>

<style>
#app {
    font-family: Arial, sans-serif;
    font-size: 12px;
    display: inline-grid;
}
</style>
