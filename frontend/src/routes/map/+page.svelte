<script lang="ts">
    import { PUBLIC_MAP_KEY } from "$env/static/public";
    import type { MarkerData } from "$lib/map/Marker.svelte";
    import Map from "$lib/map/Map.svelte";
    import type { LngLat } from "@yandex/ymaps3-types";
    import { onMount } from "svelte";
    import { fetchRoute } from "$lib/map/routing";

    const markers: MarkerData[] = [
        { id: 0, kind: "store", location: [39.719199, 47.243771] },
        { id: 1, kind: "warehouse", location: [39.718199, 47.243771] }
    ];
    let routes: LngLat[][] = [];

    onMount(async () => {
        routes.push(await fetchRoute([39.712686, 47.227726], [39.713011, 47.23939]));
        routes = routes;
    });
</script>

<Map api_key={PUBLIC_MAP_KEY} {markers} {routes} />
