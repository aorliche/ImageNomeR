<template>
    <h3>Cohort Info: {{ cohort }}</h3>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
        <div class="type">
            <h4>FC</h4>
            <div>
                {{ store.data.fc.length }} FCs 
                <span v-if="store.selected('fc')">({{ store.selected('fc').length }} selected)</span>
            </div>
            <ul>
                <li v-for="fc in filteredData.fc" :key="fc.id">
                    <input type="checkbox" v-model="fc.selected">
                    {{ fc.fname }}
                </li>
            </ul>
            <div>
                <input type="text" v-model="search.fc">
            </div>
        </div>
        <div class='options'>
            
        </div>
    </div>
</template>

<script>
import { useCohortStore } from "@/stores/CohortStore";

class Cohort {
    constructor(json) {
        this.fc = this.parseFc(json.fc);
    }
    parseFc(fc) {
        this.nfc = fc.length;
        fc.sort();
        return fc.map((fname, idx) => ({ id: idx, fname: fname, ...this.parseFname(fname) }));
    }
    parseFname(fname) {
        const parts = fname.split('_');
        const sub = parts[0];
        let task = '';
        parts.slice(1).forEach(part => {
            if (part.startsWith('task-')) {
                task = part.substr(5);
            }
        });
        return {
            sub, task
        }
    }
}

export default {
    name: 'CohortInfo',
    data() {
        return {
            error: false,
            loading: true,
            search: {fc: ''}
        }
    },
    props: {
        cohort: String
    },
    created() {
        this.fetchCohort();
    },
    setup() {
        const store = useCohortStore();
        return {
            store
        }
    },
    computed: {
        filteredData() {
            return {fc: this.store.data['fc'].filter(fc => fc.fname.includes(this.search['fc']))};
        }
    },
    methods: {
        fetchCohort() {
            fetch(`/data/info?cohort=${this.cohort}`)
                .then(resp => resp.json())
                .then(json => {
                    this.loading = false;
                    if (json.err) {
                        this.error = json.err;
                        return;
                    }
                    this.store.data = new Cohort(json);
                })
                .catch(err => this.error = err);
        }
    }
}
</script>

<style scoped>
ul {
    max-height: 100px;
    overflow-y: scroll;
}
</style>
