<script lang="ts">
    import SideBarEntry from "./SideBarEntry.svelte";
</script>

<div class="sidebar">
    <div class="top">
        <div class="logo">Logist 52</div>
        <div class="sidebar__main">
            <section class="sidebar-menu">
                <p class="Regular">Основное</p>
                <div class="main__btns">
                    <SideBarEntry path="/dashboard" name="Главная" icon="home" />
                    <SideBarEntry path="/map" name="Карта" icon="map" />
                    <SideBarEntry path="/supply" name="Заявки" icon="orders" />
                </div>
                <div class="line"></div>
                <p class="Regular">Панель администрации</p>
                <div class="main__btns">
                    <SideBarEntry path="/admin/users" name="Пользователи" icon="users" />
                    <SideBarEntry path="/admin/roles" name="Роли" icon="roles" />
                </div>
            </section>
        </div>
    </div>
    <div class="main__user">
        <SideBarEntry path="/account" name="Личный кабинет" icon="avatar">
            <!-- <img src="./icons/avatar.svg" alt="" class="avatar" /> -->
            <div class="user-role">
                <p class="Semibold user-name">Андрей Тычинин</p>
                <p class="Medium user-role-name">Администратор</p>
            </div>
        </SideBarEntry>
    </div>
</div>

<style lang="scss">
    .sidebar {
        background-color: white;
        border-radius: 25px;
        padding: 22px;
        max-width: 240px;
        min-height: 90vh;

        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .logo {
        font-weight: 900;
        font-size: 24px;
    }

    .sidebar__main {
        margin-top: 52px;
        display: flex;
        flex-direction: column;

        p {
            color: var(--dark-blue-70);
        }
    }

    .main__btns {
        margin-top: 40px;
        display: flex;
        flex-direction: column;
        gap: 12px;
        color: var(--white);
    }

    .line {
        margin: 40px 0;
        width: 196px;
        height: 1px;
        background-color: rgba(208, 206, 215, 1);
    }

    .main__user {
        display: flex;
        gap: 12px;
        .user-role {
            display: flex;
            flex-direction: column;

            .user-name {
                font-size: 14px;
                margin-bottom: 4px;
            }

            .user-role-name {
                color: var(--dark-blue-60);
            }
        }
    }
</style>
