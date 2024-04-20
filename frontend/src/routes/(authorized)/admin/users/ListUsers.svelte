<script lang="ts">
    let role = "";

    const items = [
        {
            fio: {
                url: "/icons/ava-users.svg",
                name: "Крылов Никита Евгеньевич"
            },
            num: 52000001,
            role: "Персонал склада",
            mail: "privet@gmail.com"
        },
        {
            fio: {
                url: "/icons/ava-users.svg",
                name: "Крылов Никита Евгеньевич"
            },
            num: 52000001,
            role: "Персонал склада",
            mail: "privet@gmail.com"
        },
        {
            fio: {
                url: "/icons/ava-users.svg",
                name: "Крылов Никита Евгеньевич"
            },
            num: 52000001,
            role: "Персонал склада",
            mail: "privet@gmail.com"
        },
        {
            fio: {
                url: "/icons/ava-users.svg",
                name: "Крылов Никита Евгеньевич"
            },
            num: 52000001,
            role: "Персонал склада",
            mail: "privet@gmail.com"
        },
        {
            fio: {
                url: "/icons/ava-users.svg",
                name: "Крылов Никита Евгеньевич"
            },
            num: 52000001,
            role: "Персонал склада",
            mail: "privet@gmail.com"
        }
    ];
</script>

<ul>
    <li class="li-header">
        <p>ФИО</p>
        <p>Номер сотрудника</p>
        <p>Роль</p>
        <p>Почта</p>
    </li>
    {#each items as item}
        <li>
            <p><img src={item.fio.url} alt="" /><span>{item.fio.name}</span></p>
            <p>{item.num}</p>
            <select name="" id="">
                <option selected value="">{item.role}</option>
                <option value="">Админ</option>
                <option value="">Логист</option>
            </select>
            <p>{item.mail}</p>
            <button><img class="add-user" src="/icons/edit_points.svg" alt="" /></button>
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
            align-items: center;
            grid-template-columns: 360px 214px 232px auto 50px;

            &:first-child {
                padding: 0 0 33px;
                border: none;
            }

            p:first-child {
                display: flex;
                align-items: center;
                gap: 16px;
                margin-left: 18px;
            }

            select {
                max-width: 180px;
            }
        }
    }

    ul::-webkit-scrollbar-thumb {
        width: 7px;
        height: 68px;
        border-radius: 100px;
        background-color: var(--egg-blue-90);
    }

    ul::-webkit-scrollbar-track {
        width: 2px;
        height: 100%;
        border-radius: 100px;
        background-color: var(--egg-blue-0);
    }
</style>
