<template>
    <div id='main'>
        <div v-if='store.display == "fc"'>
            <FC v-for="fc in store.selected('fc')" :key="fc.id" cohort='test' :sub='fc.sub' :task='fc.task' remap/>
        </div>
        <div v-elseif='store.display != null'>
            <Demographics cohort='text' :field='store.display'/>
        </div>
    </div>
</template>

<script>
// FC should go into explore or fcs view
import FC from './FC.vue'
import { useCohortStore } from "@/stores/CohortStore";
import Demographics from './Demographics.vue';

export default {
    name: 'MainPanel',
    components: {
    FC,
    Demographics
},
    setup() {
        const store = useCohortStore();
        return {
            store
        }
    }
}
</script>

<style scoped>
#main {
    grid-area: 1 / 2 / span 1 / span 1;
}
</style>