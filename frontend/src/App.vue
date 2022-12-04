<template>
  <v-app>
    <v-main>
        <div id='content'>
            <SidePanel/>
            <MainPanel/>
            <BottomPanel/>
        </div>
    </v-main>
  </v-app>
</template>

<script>
import SidePanel from './components/SidePanel.vue'
import MainPanel from './components/MainPanel.vue'
import BottomPanel from './components/BottomPanel.vue'

export default {
    name: 'App',
    components: {
        SidePanel,
        MainPanel,
        BottomPanel
    }
}
</script>

<style>
#content {
    font-family: Arial, sans-serif;
    font-size: 12px;
    display: inline-grid;
}
</style>
