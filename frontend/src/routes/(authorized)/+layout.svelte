<script lang="ts">
    import SideBar from "$lib/sidebar/SideBar.svelte";
</script>

<main>
    <SideBar />
    <slot />
</main>

<style>
    main {
        display: flex;
        gap: 26px;
        height: 100%;
        padding: 30px 26px 30px;

        color: rgba(46, 36, 77, 1);
        background-color: rgba(243, 242, 244, 1);
    }
</style>
