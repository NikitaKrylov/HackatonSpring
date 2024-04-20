<script lang="ts">
    import Header from "./Header.svelte";
    import List from "./List.svelte";

</script>

<main>
    <Header/>
    <List/>
</main>

<style lang="scss">
    main {
        flex: 1px;
        background: var(--white);
        padding: 35px;
        border-radius: 35px;
    }
</style>