import { defineStore } from 'pinia';

export const useCohortStore = defineStore("CohortStore", {
    state: () => {
        return {
            data: {fc: []}
        };
    },
    getters: {
        selected: (state) => {
            return (type) => state.data[type].filter(elt => elt.selected);
        }
    },
    // actions
});