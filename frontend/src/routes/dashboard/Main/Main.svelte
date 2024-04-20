<script lang=ts>
    import Categories from "./Categories/Categories.svelte";
    import Header from "./Header.svelte";
    import MainStatistic from "./Statistics/MainStatistic.svelte";
    import Stores from "./Stores.svelte";
    

</script>

<main>
    <Header/>
    <div class="wrapper">
        <div class="right-bar">
            <Stores/>
            <MainStatistic/>
        </div>
        <Categories/>
    </div>
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

    .right-bar {
        display: flex;
        flex-direction: column;
    }

    .wrapper{
        display: flex;
        justify-content: space-between;
        gap: 18px;
    }
</style>