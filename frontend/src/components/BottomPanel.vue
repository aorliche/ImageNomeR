<template>
    <div id='bottom'>
        <v-btn-toggle v-model='store.display'>
            <v-btn v-for='field in Object.keys(store.demo)' :key='field' :value='field'>
                {{ field }}
            </v-btn>
            <v-btn key='fc' value='fc'>FC</v-btn>
        </v-btn-toggle>
    </div>
</template>

<script>
import { useCohortStore } from "@/stores/CohortStore";

export default {
    name: 'BottomPanel',
    setup() {
        const store = useCohortStore();
        return {
            store
        }
    }
}
</script>

<style scoped>
#bottom {
    grid-area: 2 / 2 / span 1 / span 1;
}
select option {
    display: inline-block;
}
</style>