<script lang="ts">
    import { writable } from "svelte/store";

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


    let visible = false;

    function toggleVissible(e) {
        e.target.parentNode.lastChild.classList.toggle('hidden')
        
    }
</script>


<div>
    <header>
        <h2>Пользователи</h2>
        <p>Создавайте новых пользователей, управляйте ими и их ролями</p>
    </header>
    <button class="send">
        <img src="/icons/add-contact.svg" alt="" />
        <p>Добавить пользователя</p>
    </button>
</div>
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
            <select name="" id="">~
                <option selected value="">{item.role}</option>
                <option value="">Админ</option>
                <option value="">Логист</option>
            </select>
            <p>{item.mail}</p>
            <button on:click={toggleVissible} >
                <img class="add-user" src="/icons/edit_points.svg" alt="" />
                <div class="hidden btn-add">
                    <button>Редактировать</button>
                    <button>Удалить</button>
                </div>
            </button>
        </li>
    {/each}
</ul>

<style lang="scss">

    

    .btn-add{
        display: flex;
        gap: 4px;
        flex-direction: column;
        align-items: end;
        position: absolute;
        right: 40px;
        top: 20px;
        


        button{
            background-color: var(--dark-blue-40);
            padding: 6px;
            width: max-content;
            border-radius: 8px;
            font-size: 14px;
        }
    }

    .hidden{
        display: none;
    }

    ul {
        max-width: 100%;
        max-height: 86.5%;
        overflow: auto;

        li {
            position: relative;
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

    div {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    header {
        margin-bottom: 46px;
    }

    h2 {
        font-weight: 700;
        font-size: 30px;
        margin-bottom: 8px;
    }

    p {
        font-weight: 500;
        font-size: 14px;
    }

   .send {
        display: flex;
        gap: 19px;

        background-color: var(--egg-blue-100);
        padding: 15px 20px;
        color: var(--white);
        border-radius: 15px;
    }

</style>
