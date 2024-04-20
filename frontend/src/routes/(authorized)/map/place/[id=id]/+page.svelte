<script lang="ts">
    import Busy from "$lib/components/Busy.svelte";
    import { selected_places } from "$lib/map/Marker.svelte";
    import type { PageServerData } from "./$types";

    export let data: PageServerData;

    $: $selected_places = [data.placement.id];
</script>

<section>
    <header>
        <a href="/map" on:click={() => ($selected_places = [])}>
            <img src="/icons/arrow_left.svg" alt="Назад" />
            <span>Назад</span>
        </a>
        <h1>{data.placement.name}</h1>
    </header>
    <div>
        <h2>Название</h2>
        <span>{data.placement.name}</span>
    </div>
    <div>
        <h2>Тип локации</h2>
        <span>
            {#if data.placement.placement_type === "storage"}
                Склад
            {:else}
                Точка продаж
            {/if}
        </span>
    </div>
    <div>
        <h2>Индивидуальный номер локации</h2>
        <span>{data.placement.id}</span>
    </div>
    <div>
        <h2>Адрес</h2>
        <span>{data.placement.address}</span>
    </div>
    {#if data.placement.placement_type === "storage"}
        <div>
            <div class="busy">
                <span>Загруженность</span>
                <Busy current={data.placement.workload} maximum={data.placement.capacity} />
            </div>
            <p>
                На складе находится {data.placement.workload} единиц ваших товаров из {data
                    .placement.capacity} возможных.
            </p>
        </div>
    {/if}
</section>

<style lang="scss">
    section {
        display: flex;
        flex-direction: column;
        max-width: 400px;
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
