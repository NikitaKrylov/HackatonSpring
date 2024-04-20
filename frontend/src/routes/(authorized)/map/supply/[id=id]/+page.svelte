<script lang="ts">
    import { selected_places } from "$lib/map/Marker.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;

    $: $selected_places = data.locations.map(x => x.id);
</script>

Supply
