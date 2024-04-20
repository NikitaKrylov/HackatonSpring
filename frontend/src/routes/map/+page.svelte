<script lang="ts">
    import type { Supply } from "$lib";
    import { getContext } from "svelte";
    import type { Writable } from "svelte/store";
    import Status from "$lib/components/Status.svelte";
    import { goto } from "$app/navigation";

    let collapsed = getContext<Writable<boolean>>("collapsed");

    const supplies: Supply[] = [
        { id: 0, date: "20 апреля", status: "Ожидает", stops: 5 },
        { id: 1, date: "20 апреля", status: "Завершено", stops: 5 },
        { id: 2, date: "20 апреля", status: "В работе", stops: 5 },
        { id: 3, date: "20 апреля", status: "Ожидает", stops: 5 }
    ];
</script>

<section>
    <header>
        <button on:click={() => ($collapsed = true)}>
            <img src="/icons/collapse.svg" alt="Скрыть" />
        </button>
        <h2>Последние заявки</h2>
    </header>
    <table>
        <tr>
            <th>№ заявки</th>
            <th>Дата</th>
            <th>Статус</th>
            <th>Кол-во пунктов</th>
        </tr>
        {#each supplies as supply}
            <tr on:click={() => goto(`/map/supply/${supply.id}`)}>
                <td>{supply.id}</td>
                <td>{supply.date}</td>
                <td><Status status={supply.status} /></td>
                <td>{supply.stops}</td>
            </tr>
        {/each}
    </table>
</section>

<style lang="scss">
    section {
        display: flex;
        flex-direction: column;
        gap: 20px;

        overflow: scroll;
        header {
            display: flex;
            gap: 8px;
            button {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 28px;
                height: 28px;
            }
            h2 {
                font-size: 26px;
            }
            padding: 22px;
        }
        table {
            border-spacing: 0;
            tr {
                border-bottom: 1px solid var(--dark-blue-50);
                &:first-of-type {
                    padding-bottom: 36px;
                }
                &:not(:first-of-type):hover {
                    cursor: pointer;
                    td {
                        background-color: var(--dark-blue-10);
                        border: 0;
                    }
                }
            }
            th {
                color: var(--dark-blue-60);
                font-size: 14px;
                font-weight: 400;
                text-align: start;
                padding: 0 48px 6px 0;
                &:first-child {
                    padding-left: 22px;
                }
            }
            td {
                font-size: 16px;
                padding: 16px 48px 28px 0;
                &:first-child {
                    padding-left: 22px;
                }
                &:last-child {
                    padding-right: 22px;
                }
            }
        }
    }
</style>
