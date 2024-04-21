<script lang="ts">
    import { fetchPlacements, type Placement } from "$lib/data/placement";
    import { onMount } from "svelte";
    import Categories from "./Categories/Categories.svelte";
    import Header from "./Header.svelte";
    import MainStatistic from "./Statistics/MainStatistic.svelte";
    import Stores from "./Stores.svelte";
    import Table from "./Table.svelte";

    let placements: Placement[] = [];
    onMount(async () => {
        placements = await fetchPlacements();
    });
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
    <Table />
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
