<script lang="ts">
    import { onMount } from "svelte";
    import { fetchOffers, type Offer } from "$lib/data/offer";

    let items: Offer[] = [];
    onMount(async () => {
        items = await fetchOffers();
    });
</script>

<ul>
    <li class="li-header">
        <p>№</p>
        <p>Позиция</p>
        <p>Id товара</p>
        <p>Заказчик</p>
        <p>Адрес</p>
        <p>Количество</p>
    </li>
    {#each items as item, i}
        <li>
            <p>{i + 1}</p>
            <p>{item.product.name}</p>
            <p>{item.product.sku}</p>
            <p>{item.product.manufactor}</p>
            <p>{item.placement.address}</p>
            <p>{item.product.product_amount} {item.product.product_measure}</p>
        </li>
    {/each}
</ul>

<style lang="scss">
    ul {
        max-width: 100%;
        max-height: 86.5%;
        overflow: auto;

        li {
            border: 1px solid var(--dark-blue-40);
            padding: 33px 0;
            display: grid;
            grid-template-columns: 80px 110px 110px 300px auto 250px;

            &:first-child {
                padding: 0 0 33px;
                border: none;
            }

            p:nth-child(1) {
                padding-left: 15px;
            }
            p:nth-child(2) {
                padding-right: 20px;
            }

            p:nth-child(4) {
                padding-right: 8px;
            }

            p:nth-child(5) {
                max-width: 250px;
            }

            
        }
    }

    ::-webkit-scrollbar-thumb {
        width: 7px;
        height: 68px;
        border-radius: 100px;
        background-color: var(--egg-blue-90);
    }

    ::-webkit-scrollbar-track {
        width: 2px;
        height: 100%;
        border-radius: 100px;
        background-color: var(--egg-blue-0);
    }
</style>
