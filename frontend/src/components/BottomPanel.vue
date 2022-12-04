<template>
    <div id='bottom'>
            <input type='radio' name='display' v-for='field in Object.keys(store.demo)' :key='field' :value='field'> {{ field }}
            <input type='radio' name='display' key='fc' value='fc'>FC
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