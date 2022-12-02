<template>
    <h3>
        {{ cohort }} cohort 
        <span v-if="!loading && !error">({{ store.subs.size }} subjects)</span>
    </h3>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
        <div class="type">
            <h4>FC</h4>
            <div>
                {{ store.fc.length }} FCs 
                <span v-if="store.selected('fc')">({{ store.selected('fc').length }} selected)</span>
            </div>
            <ul>
                <li v-for="fc in filteredFC.fc" :key="fc.id">
                    <input type="checkbox" v-model="fc.selected">
                    {{ fc.fname }}
                </li>
            </ul>
            <div>
                <input type="text" v-model="search.fc">
            </div>
        </div>
        <div class='demographics'>
            <h4>Demographics</h4>
            <ul>
                <li v-for="field in Object.keys(store.demo)" :key="field">
                    <strong>{{ field }}</strong> {{ store.summary(field) }}
                </li>
            </ul>
        </div>
        <div class='groups'>
            <h4>Groups</h4>
            <div>
                Group SQL 
                <input type='text' v-model="query">
                <button @click='makeGroup'>Create</button>
            </div>
            <ol>
                <li v-for="group in store.groups" :key="group.query">
                    <input type="checkbox" v-model="group.selected">
                    {{ group.query }} ({{ group.subs.length }})
                </li>
            </ol>
        </div>
    </div>
</template>

<script>
import { useCohortStore } from "@/stores/CohortStore";

export default {
    name: 'CohortInfo',
    data() {
        return {
            error: false,
            loading: true,
            search: {fc: ''},
            query: '',
            active: null
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
        filteredFC() {
            return {fc: this.store.fc.filter(fc => fc.fname.includes(this.search['fc']))};
        }
    },
    methods: {
        activate(group) {
            this.active = group;
        },
        fetchCohort() {
            fetch(`/data/info?cohort=${this.cohort}`)
            .then(resp => resp.json())
            .then(json => {
                this.loading = false;
                if (json.err) {
                    this.error = json.err;
                    return;
                }
                this.store.fc = this.parseFC(json.fc);
                this.store.demo = json.demo;
                this.store.subs = this.getSubs(json.demo);
            })
            .catch(err => this.error = err);
        },
        getSubs(demo) {
            const subs = new Set();
            for (let key in demo) {
                Object.keys(demo[key]).forEach(sub => subs.add(sub));
            }
            return subs;
        },
        makeGroup() {
            fetch(`/data/group?cohort=${this.cohort}&query=${this.query}`)
            .then(resp => resp.json())
            .then(json => {
                if (json.err) {
                    alert(json.err);
                    return;
                }
                this.store.groups.push({query: this.query, subs: json});
            })
            .catch(err => alert(err));
        },
        parseFC(fc) {
            fc.sort();
            return fc.map((fname, idx) => ({ id: idx, fname: fname, ...this.parseFname(fname) }));
        },
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
}
</script>

<style scoped>
ul {
    max-height: 100px;
    overflow-y: scroll;
}
</style>
