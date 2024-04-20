<script lang="ts" context="module">
    import type { LngLat } from "@yandex/ymaps3-types";

    export type MarkerData = {
        id: number;
        kind: "warehouse" | "store";
        location: LngLat;
    };

    export let selected_places = writable<number[]>([]);
</script>

<script lang="ts">
    import { createEventDispatcher, onMount } from "svelte";
    import { writable } from "svelte/store";

    export let data: MarkerData;
    let path: string;

    onMount(() => {
        console.log($selected_places);
    });

    $: {
        if ($selected_places.includes(data.id)) {
            path = "selected";
        } else if (data.kind === "warehouse") {
            path = "warehouse";
        } else if (data.kind === "store") {
            path = "store";
        } else {
            path = "warehouse"; // Just in case
        }
        path = `/markers/${path}.svg`;
    }

    const dispatch = createEventDispatcher<{ click: void }>();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="marker" data-id={data.id} on:click={() => dispatch("click")}>
    <img src={path} alt="" />
</div>

<style lang="scss">
    .marker {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;

        width: 0;
        height: 0;

        img {
            position: absolute;
            bottom: 0;
            width: 48px;
        }
    }
</style>
