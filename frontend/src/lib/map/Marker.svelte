<script lang="ts" context="module">
    import type { LngLat } from "@yandex/ymaps3-types";

    export type MarkerData = {
        id: number;
        kind: "warehouse" | "store";
        location: LngLat;
    };
</script>

<script lang="ts">
    import { createEventDispatcher } from "svelte";

    export let data: MarkerData;
    $: img_src = data.kind === "warehouse" ? "/icons/warehouse.svg" : "/icons/store.svg";

    const dispatch = createEventDispatcher<{ click: void }>();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="marker" data-id={data.id} on:click={() => dispatch("click")}>
    <img src={img_src} alt="" />
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
