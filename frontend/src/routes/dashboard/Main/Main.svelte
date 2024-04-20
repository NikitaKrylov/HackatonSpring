<script>
    import Header from "./Header.svelte";
    import Stores from "./Stores.svelte";

</script>

<main>
    <Header/>
    <Stores/>
</main>

<style>
    main {
        width: 100%;
        display: flex;
        background-color: var(--white);
        border-radius: 25px;

        padding: 35px 22px;
    }
</style>