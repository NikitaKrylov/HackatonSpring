<script>
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
        }
    ]
</script>

<section>
    <header>
        <h2>Последние заявки</h2>
    </header>

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
</section>

<style lang="scss">
    section{
        flex: 1px;
        background: var(--white);
        padding: 35px;
        border-radius: 35px;
        max-height: min-content;
    }

    header{
        margin-bottom: 46px;
        
        h2{
            font-weight: 700;
            font-size: 30px;
            margin-bottom: 8px;
        }
    }

    ul{
        max-width: 100%;
        max-height: 40.5%;
        overflow: hidden;

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

</style>