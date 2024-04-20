<script lang="ts">
    import "../app.scss";
    import SideBar from "./SideBar.svelte";
</script>


<main>
    <SideBar/>
    <slot />
</main>

<style>
    main{
        display: flex;
        gap: 26px;
        justify-content: space-between;
    }
</style>