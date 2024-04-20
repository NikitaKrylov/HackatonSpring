<script lang="ts">
    import { PUBLIC_MAP_KEY } from "$env/static/public";
    import { selected_places, type MarkerData } from "$lib/map/Marker.svelte";
    import Map from "$lib/map/Map.svelte";
    import type { LngLat } from "@yandex/ymaps3-types";
    import { onMount } from "svelte";
    import { goto } from "$app/navigation";

    let markers: MarkerData[] = [
        { id: 0, kind: "store", location: [39.719199, 47.243771] },
        { id: 1, kind: "warehouse", location: [39.718199, 47.243771] }
    ];
    let routes: LngLat[][] = [];

    onMount(() => {
        return () => {
            $selected_places = [];
        };
    });

    $: {
        $selected_places;
        markers = markers;
        routes = routes;
    }
</script>

<section>
    <Map
        api_key={PUBLIC_MAP_KEY}
        {markers}
        {routes}
        on:click={e => goto(`/map/place/${e.detail.id}`)}
    />
    <div>
        <slot />
    </div>
</section>

<style lang="scss">
    section {
        flex: 1;
        border-radius: 25px;
        overflow: hidden;
        position: relative;
        div {
            position: absolute;
            right: 0;
            top: 0;
            border-radius: 25px;
            background-color: white;
            overflow-x: hidden;
            overflow-y: scroll;
        }
    }
</style>
