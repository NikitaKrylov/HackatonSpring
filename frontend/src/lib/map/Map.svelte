<script lang="ts">
    import type { LngLat, YMap, YMapFeature, YMapMarker } from "@yandex/ymaps3-types";
    import type { MarkerData } from "./Marker.svelte";
    import { createEventDispatcher, onMount } from "svelte";
    import { addLine } from "./routing";
    import { addMarker } from "./marker";

    let mapElem: HTMLElement;
    let map: YMap | undefined = undefined;
    export let center: LngLat = [39.720358, 47.222078];
    export let zoom: number = 10;

    export let markers: MarkerData[] = [];
    let markers_features: YMapMarker[] = [];
    $: {
        if (map !== undefined) {
            const _map = map;
            markers_features.forEach(feat => _map.removeChild(feat));
            markers_features = markers.map(marker =>
                addMarker(_map, marker, () => dispatch("click", marker))
            );
        }
    }

    export let routes: LngLat[][] = [];
    let lines: YMapFeature[] = [];
    $: {
        if (map !== undefined) {
            const _map = map;
            lines.forEach(line => _map.removeChild(line));
            lines = routes.map(route => addLine(_map, route));
        }
    }

    export let api_key: string;
    $: api_src = `https://api-maps.yandex.ru/v3/?apikey=${api_key}&lang=ru_RU`;

    onMount(async () => {
        if (map === undefined) {
            await ymaps3.ready;
        }

        map = new ymaps3.YMap(mapElem, {
            location: { center, zoom }
        });

        const { YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer, YMapLayer } = ymaps3;

        map.addChild(new YMapDefaultSchemeLayer({}))
            .addChild(new YMapDefaultFeaturesLayer({}))
            .addChild(new YMapLayer({ type: "markers", zIndex: 1800 }));
    });

    const dispatch = createEventDispatcher<{ click: MarkerData }>();
</script>

<svelte:head>
    <script src={api_src}></script>
</svelte:head>

<div bind:this={mapElem} />

<style lang="scss">
    div {
        width: 100%;
        height: 100%;
    }
</style>
