<script lang="ts">
    import type { PageData } from "./$types";
    import ListUsers from "./ListUsers.svelte";

    export let data: PageData;
</script>

<main>
    <ListUsers users={data.users} />
</main>

<style lang="scss">
    main {
        border-radius: 35px;
        flex: 1;
        background-color: var(--white);
        padding: 35px;
    }
</style>
