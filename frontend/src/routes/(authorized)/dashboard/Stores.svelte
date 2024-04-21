<script lang="ts">
    import Busy, { getColor, getColorBack } from "$lib/components/Busy.svelte";
    import type { Placement } from "$lib/data/placement";

    export let placements: Placement[];
    $: entries = placements.filter(x => x.placement_type === "storage");
    $: entries.length = Math.min(entries.length, 3);
</script>

<section>
    <a class="seealso" href="/map">Смотреть всё</a>
    <div class="stores">
        {#each entries as entry}
            <a
                class="card"
                style:background-color={getColorBack(entry.workload, entry.capacity)}
                href={`/map/place/${entry.id}`}
            >
                <h3>{entry.name}</h3>
                <div class="busy">
                    <p>Загруженность</p>
                    <Busy current={entry.workload} maximum={entry.capacity} />
                </div>
                <p>Обработал 20 заявок на прошлой неделе</p>
            </a>
        {/each}
    </div>
</section>

<style lang="scss">
    section {
        max-width: 100%;
        text-align: right;

        .seealso {
            display: block;
            color: var(--egg-blue-100);
            position: relative;
            margin-bottom: 16px;
            padding-right: 14px;
            text-decoration: none;

            &::after {
                content: "";
                position: absolute;
                display: inline-block;
                background-image: url("/icons/arrow-right.svg");
                background-repeat: no-repeat;
                width: 7px;
                height: 14px;
                right: 0;
                top: 4px;
            }
        }

        .stores {
            display: flex;
            justify-content: space-between;
            gap: 8px;

            .card {
                font-size: 0.875;
                max-width: 14rem;
                background: rgba(228, 248, 230, 1);
                border-radius: 35px;
                text-align: center;
                padding: 20px 12px 16px;
            }

            h3 {
                font-size: 1.2rem;
                margin-bottom: 0.625rem;
            }

            p {
                display: inline-block;
                font-size: 14px;
            }

            .busy {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 18px;
                margin-bottom: 0.625rem;
                font-size: 14px;
            }
        }
    }
</style>
