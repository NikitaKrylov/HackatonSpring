<script lang="ts">
    import Categories from "./Categories/Categories.svelte";
    import Header from "./Header.svelte";
    import MainStatistic from "./Statistics/MainStatistic.svelte";
    import Stores from "./Stores.svelte";
    import Table from "./Table.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;
    $: placements = data.placements;
    $: offers = data.offers;
</script>

<main>
    <Header />
    <div class="wrapper">
        <div class="left-bar">
            <Stores {placements} />
            <MainStatistic />
        </div>
        <Categories />
    </div>
    <Table {offers} />
</main>

<style lang="scss">
    main {
        flex: 1;
        background-color: var(--white);
        display: flex;
        flex-direction: column;
        border-radius: 25px;

        padding: 35px 22px;
    }

    .left-bar {
        display: flex;
        flex-direction: column;
        max-width: 45rem;
    }

    .wrapper {
        max-width: 45.25rem;
        display: flex;
        justify-content: space-between;
        gap: 18px;
    }
</style>
