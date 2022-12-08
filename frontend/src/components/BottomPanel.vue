<template>
    <v-container>
        <v-btn-toggle v-model='store.display'>
            <v-btn v-for='field in Object.keys(store.demo)' :key='field' :value='field'> 
                {{ field }}
            </v-btn>
            <v-btn key='fc' value='fc'>FC</v-btn>
        </v-btn-toggle>
        <v-card title='Correlation' id='correlation'>
            <v-card-subtitle>Find correlation between demographic features and FC for group</v-card-subtitle>
            <v-row align='center' class='padded'>
                <v-select cols='3' :items='store.groups' item-title='query' label='Group' hide-details dense class='padded'>
                </v-select>
                <v-select 
                    cols='3'
                    :items='Object.keys(store.demo)' 
                    label='Demographic Feature' 
                    hide-details dense class='padded'>
                </v-select>
                <v-select 
                    cols='3'
                    :items="Object.keys(store.demo).concat(['fc'])" 
                    label='Response Var' 
                    hide-details dense class='padded'>
                </v-select>
                <v-btn cols='2' key='go' value='Go' class='padded-alt'>Go</v-btn>
            </v-row>
        </v-card>
    </v-container>
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
#correlation {
    max-width: 800px;
}
</style>