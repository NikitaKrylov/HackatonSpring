<script lang="ts">
    import Status from "$lib/components/Status.svelte";
    import { selected_places } from "$lib/map/Marker.svelte";
    import { getContext, onMount } from "svelte";
    import type { PageServerData } from "./$types";
    import type { Writable } from "svelte/store";
    import type { LngLat } from "@yandex/ymaps3-types";
    import { fetchRoute } from "$lib/map/routing";

    export let data: PageServerData;

    const routes = getContext<Writable<LngLat[][]>>("routes");

    onMount(async () => {
        let ids = [data.supply.storage_id, ...data.supply.offers.map(x => x.placement_id)];
        $selected_places = ids;

        // FIXME: N^2!
        let placements = data.placements.filter(x => ids.includes(x.id));
        let coords: LngLat[] = placements.map(x => x.coord);
        $routes = [await fetchRoute(coords)];
    });
    onMount(() => () => ($routes = []));
</script>

<section>
    <header>
        <a href="/map">
            <img src="/icons/arrow_left.svg" alt="Назад" />
            <span>Назад</span>
        </a>
        <h1>Заявка №{data.supply.id}</h1>
        <Status status={data.supply.supply_status} />
    </header>
    <div>
        <h2>Номер заявки</h2>
        <span>{data.supply.id}</span>
    </div>
    <div>
        <h2>Статус</h2>
        <Status status={data.supply.supply_status} />
    </div>
    <div>
        <h2>Запланированная дата перевозки</h2>
        <span>{data.supply.created_at}</span>
    </div>
    <div>
        <h2>Количество пунктов в маршруте</h2>
        <span>{data.supply.offers.length}</span>
    </div>
    <div>
        <h2>Товары в заявке</h2>
        <ul>
            {#each data.supply.offers as offer}
                <li>{offer.product_id}</li>
            {/each}
        </ul>
    </div>
</section>

<style lang="scss">
    section {
        display: flex;
        flex-direction: column;
        gap: 35px;
        padding: 22px;

        header {
            display: flex;
            align-items: center;
            gap: 24px;
            a {
                display: flex;
                align-items: center;
                color: var(--dark-blue-70);
                text-decoration: none;
                font-size: 14px;
            }
            h1 {
                color: var(--dark-blue-100);
                font-size: 26px;
                font-weight: 700;
            }
        }
        > div {
            display: flex;
            flex-direction: column;
            gap: 6px;
            h2 {
                color: var(--dark-blue-60);
                font-size: 14px;
                font-weight: 400;
            }
            span {
                color: var(--dark-blue-90);
                font-size: 16px;
            }
            p {
                color: var(--dark-blue-60);
                font-size: 14px;
                margin-top: 7px;
            }
            .busy {
                display: flex;
                gap: 30px;
                align-items: center;
            }
        }
    }
</style>
