<script lang="ts">
    import Header from "./Header.svelte";
    import ListUsers from "./ListUsers.svelte";
</script>

<main>
    <Header />
    <ListUsers />
</main>

<style lang="scss">
    main {
        border-radius: 35px;
        flex: 1;
        background-color: var(--white);
        padding: 35px;
    }
</style>
