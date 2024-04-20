<script lang="ts">
    import Main from "./dashboard/Main/Main.svelte";
</script>

<div class="wrapper">
    <div class="sidebar">
        <div class="top">
            <div class="logo">Logist 52</div>
            <div class="sidebar__main">
                <section class="sidebar-menu">
                    <p class="Regular">Основное</p>
                    <div class="main__btns">
                        <button class:active={true} class="btn-main"><img src="/icons/home.svg" />Главная</button>
                        <button class:active={false} class="btn-map"><img src="/icons/map.svg" />Карта</button>
                        <button class:active={false} class="btn-orders"><img src="/icons/orders.svg" />Заказы</button>
                    </div>
                    <div class="line"></div>
                    <p class="Regular">Панель администрации</p>
                    <div class="main__btns">
                        <button class:active={false} class="btn-users"><img src="/icons/users.svg" />Пользователи</button>
                        <button class:active={false} class="btn-roles"><img src="/icons/roles.svg" />Роли</button>
                    </div>
                </section>
            </div>
        </div>
        <div class="main__user">
            <img src="" alt="" class="avatar">
            <img src="./icons/avatar.svg" alt="" class="avatar">
            <div class="user-role">
                <p class="Semibold user-name">Абдукарим Ашотович</p>
                <p class="Medium user-role-name">Администратор</p>
            </div>
        </div>
    </div>
    <Main/>
</div>

<style lang="scss">
.wrapper {
    display: flex;
    justify-content: space-between;
}

.sidebar{
    background-color: white;
    border-radius: 25px;
    padding: 22px;
    max-width: 240px;
    min-height: 90vh;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.logo{
    font-weight: 900;
    font-size: 24px;
}

.sidebar__main{
    margin-top: 52px;
    display: flex;
    flex-direction: column;

    p{
        color: var(--dark-blue-70);
    }
}

.main__btns{
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    gap: 25px;
    color: var(--white);
}

.line {
        margin: 40px 0;
        width: 196px;
        height: 1px;
        background-color: rgba(208, 206, 215, 1);
    }

button {
    display: flex;
    text-align: center;
    gap: 18px;
    color: var(--dark-blue-90);
    padding: 0 16px;

    &.active{
        padding: 12px 16px;
        background-color: var(--egg-blue-100);
        border-radius: 15px;
        color: var(--white);
    }
}

.main__user{
    display: flex;
    gap: 12px;
    .user-role{
        display: flex;
        flex-direction: column;

        .user-name{
            font-size: 14px;
            margin-bottom: 4px;
        }

        .user-role-name{
            color: var(--dark-blue-60);
        }
    }
}



</style>