<template>
    <div id='bottom'>
        <select multiple>
            <option>Demographics</option>
            <option>FC</option>
        </select>
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