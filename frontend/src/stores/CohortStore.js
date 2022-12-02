import { defineStore } from 'pinia';

export const useCohortStore = defineStore("CohortStore", {
    state: () => {
        return {
            fc: [], 
            demo: {},
            subs: [],
            groups: []
        };
    },
    getters: {
        selected: (state) => {
            return (type) => state[type].filter(elt => elt.selected);
        },
        summary: (state) => {
            return (field) => {
                const vals = Object.values(state.demo[field]);
                if (!isNaN(vals[0])) {
                    const min = Math.min(...vals);
                    const max = Math.max(...vals);
                    const mean = vals.reduce((prev, cur) => prev+cur, 0)/vals.length;
                    return `n=${vals.length} min: ${min} mean: ${mean} max: ${max}`;
                } else if (vals[0] == 'M') {
                    let m = 0;
                    let f = 0;
                    vals.forEach(val => {
                        if (val == 'M') m++;
                        else if (val == 'F') f++;
                    });
                    return `n=${vals.length} male: ${m} female: ${f}`
                }
            }
        }
    },
    // actions
});