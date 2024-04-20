<script lang="ts">
    import { PUBLIC_MAP_KEY } from "$env/static/public";
    import { selected_places, type MarkerData } from "$lib/map/Marker.svelte";
    import Map from "$lib/map/Map.svelte";
    import type { LngLat } from "@yandex/ymaps3-types";
    import { onMount, setContext } from "svelte";
    import Collapsed from "./Collapsed.svelte";
    import { writable } from "svelte/store";
    import { goto, onNavigate } from "$app/navigation";

    let collapsed = writable(false);
    setContext("collapsed", collapsed);

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
        on:click={e => {
            $collapsed = false;
            goto(`/map/warehouse/${e.detail.id}`);
        }}
    />
    {#if $collapsed}
        <Collapsed on:expand={() => ($collapsed = false)} />
    {:else}
        <div>
            <slot />
        </div>
    {/if}
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
            bottom: 0;
            border-radius: 25px;
            background-color: white;
        }
    }
</style>
