<script lang=ts>
    import Header from "./Header.svelte";
    import MainStatistic from "./Statistics/MainStatistic.svelte";
    import Stores from "./Stores.svelte";

</script>

<main>
    <Header/>
    <Stores/>
    <MainStatistic/>
</main>

<style lang="scss">
    main {
        width: 100%;
        display: flex;
        flex-direction: column;
        background-color: var(--white);
        border-radius: 25px;

        padding: 35px 22px;
    }
</style>