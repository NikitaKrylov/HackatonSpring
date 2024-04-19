<script lang="ts">
    import "../app.scss";
    import SideBar from "./SideBar.svelte";
</script>

<slot />
<main>
    <SideBar/>
</main>