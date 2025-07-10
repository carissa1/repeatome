// import algoliasearch from 'algoliasearch/lite';
// import { autocomplete } from '@algolia/autocomplete-js';

window.addEventListener('DOMContentLoaded', () => {
    const searchClient = algoliasearch('I8J408MSCM', '7a38c6848180ee8d3723175b5ec3cc4e');

    const proteinIndex = searchClient.initIndex('proteinTF');
    const repeatIndex = searchClient.initIndex('repeat');
    const referenceIndex = searchClient.initIndex('referenc');
    const organismIndex = searchClient.initIndex('organism');

    console.log('algoliasearch:', typeof algoliasearch);
    console.log('searchClient:', searchClient);
    console.log('index:', proteinIndex);
    console.log('autocomplete:', typeof autocomplete);

    autocomplete({
    container: '#algolia-search-input',
    placeholder: 'Search a protein or repeat',
    getSources({ query }) {
        return [
        {
            sourceId: 'proteinTF',
            getItems() {
            return proteinIndex.search(query, { hitsPerPage: 5 }).then(res => res.hits);
            },
            templates: {
            header() {
                return '<div class="aa-header">Proteins</div>';
            },
            item({ item }) {
                str = item.gene;
                return "<a href='" + item.url + "'><div>" + str + "</div></a>";
            }
            }
        },
        {
            sourceId: 'repeat',
            getItems() {
            return repeatIndex.search(query, { hitsPerPage: 3 }).then(res => res.hits);
            },
            templates: {
            header() {
                return '<div class="aa-header">Repeat</div>';
            },
            item({ item }) {
                str = item.name;
                return "<a href='" + item.url + "'><div>" + str + "</div></a>";
            }
            }
        },
        {
            sourceId: 'reference',
            getItems() {
            return referenceIndex.search(query, { hitsPerPage: 2 }).then(res => res.hits);
            },
            templates: {
            header() {
                return '<div class="aa-header">Reference</div>';
            },
            item({ item }) {
                str = item.title;
                return "<a href='" + item.url + "'><div>" + str + "</div></a>";
            }
            }
        },
        {
            sourceId: 'organism',
            getItems() {
            return organismIndex.search(query, { hitsPerPage: 2 }).then(res => res.hits);
            },
            templates: {
            header() {
                return '<div class="aa-header">Organism</div>';
            },
            item({ item }) {
                str = item.scientific_name;
                return "<a href='" + item.url + "'><div>" + str + "</div></a>";
            }
            }
        },
        ];
    }
    });
});