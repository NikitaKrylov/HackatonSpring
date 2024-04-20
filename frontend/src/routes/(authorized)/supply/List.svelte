<script lang="ts">
    const items = [
        {
            num: 2000,
            position: 'apples',
            id: 1,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
        {
            num: 2000,
            position: 'apples',
            id: 2,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
        {
            num: 2000,
            position: 'apples',
            id: 3,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
        {
            num: 2000,
            position: 'apples',
            id: 4,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
        {
            num: 2000,
            position: 'apples',
            id: 5,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
        {
            num: 2000,
            position: 'apples',
            id: 6,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
        {
            num: 2000,
            position: 'apples',
            id: 7,
            order: 'pyaterochka',
            address: 'улица Ленинский проспект, дом 52, корпус 3',
            count: 120
        },
    ]
</script>

<ul>
    <li class="li-header">
        <p>№ заявки</p>
        <p>Позиция</p>
        <p>Id товара</p>
        <p>Заказчик</p>
        <p>Адрес</p>
        <p>Количество </p>
    </li>
    {#each items as item}
        <li>
            <p>{item.num}</p>
            <p>{item.position}</p>
            <p>{item.id}</p>
            <p>{item.order}</p>
            <p>{item.address}</p>
            <p>{item.count}</p>
        </li>
    {/each}
</ul>

<style lang="scss">
    ul{
        max-width: 100%;
        max-height: 86.5%;
        overflow: auto;

        li{
            border: 1px solid var(--dark-blue-40);
            padding: 33px 18px;
            display: grid;
            grid-template-columns: 130px 187px 126px 172px 295px auto;

            &:first-child{
                padding: 0 0 33px;
                border: none;
            }

            p:nth-child(5){
                max-width: 250px;
            }
            
            p:nth-child(6){
                text-align: center;
            }

        }
    }

    ::-webkit-scrollbar-thumb {
        width: 7px;
        height: 68px;
        border-radius: 100px;
        background-color: var(--egg-blue-90);
    }

    ::-webkit-scrollbar-track{
        width: 2px;
        height: 100%;
        border-radius: 100px;
        background-color: var(--egg-blue-0);
    }


</style>