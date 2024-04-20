<script lang="ts">
    import { page } from "$app/stores";
    import { selected_places } from "$lib/map/Marker.svelte";

    $: id = Number($page.params.id);
    $: $selected_places = [id];
</script>

Warehouse
