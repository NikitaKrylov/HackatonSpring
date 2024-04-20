<script lang="ts">
    import Role from "./Role.svelte";
    const tasks = ['Управление пользователями','Управление ролями','Управление поставками','Администрирование заявок']
    
</script>

<section>
    <header>Роли</header>
    <div class="roles">
        <Role {tasks} name='Администратор'/>
        <Role {tasks} name='Логист'/>
        <Role {tasks} name='Аналитик'/>
        <Role {tasks} name='Персонал склада'/>
        <button>
            <img src="/icons/plus.svg" alt="plus">
            <p>Создать новую роль</p>
        </button>
    </div>
</section>

<style lang="scss">
    section{
        flex: 1px;
        padding: 35px;
        background-color: var(--white);
        border-radius: 35px;

        header{
            font-weight: 700;
            font-size: 30px;
            margin-bottom: 2rem;
        }

        .roles {
            margin: 0 auto;
            max-width: 65.6rem;
            display: flex;
            flex-wrap: wrap;
            gap: 18px;

            button{
                max-width: 17.3rem;

                border: 2px solid var(--egg-blue-70);
                border-radius: 35px;
                padding: 82px 47px;
                color: var(--egg-blue-80);
                font-weight: 600;
                font-size: 22px;

                display: flex;
                flex-direction: column;
                justify-content: space-between;
                align-items: center;
            }
        }
    }
</style>