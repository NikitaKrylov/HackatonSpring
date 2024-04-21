<script lang="ts">
    import { deleteUser, setUserRole, type User } from "$lib/data/user";
    import type { PageData } from "./$types";

    export let data: PageData;

    function toggleVissible(e: any) {
        e.target.parentNode.lastChild.classList.toggle("hidden");
    }
    function onChange(user: User) {
        user.role = data.roles.find(x => x.id === user.role.id)!;
        if (user.role !== null) setUserRole(user.id, user.role.id);
    }
</script>

<main>
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
        {#each data.users as user}
            <li>
                <p>
                    <img src={"/icons/user_icon.svg"} alt="" />
                    <span>{user.last_name} {user.first_name} {user.middle_name}</span>
                </p>
                <p>{user.id}</p>
                <select bind:value={user.role.id} on:change={() => {}}>
                    {#each data.roles as role}
                        <option value={role.id}>{role.name}</option>
                    {/each}
                </select>
                <p>{user.login}</p>
                <button class="hidden" on:click={toggleVissible}>
                    <img class="add-user" src="/icons/edit_points.svg" alt="" />
                    <div class="hidden btn-add">
                        <button on:click|stopPropagation={() => {}}> Редактировать </button>
                        <button
                            on:click|stopPropagation={() => {
                                data.users = data.users.filter(x => x.id !== user.id);
                                deleteUser(user.id);
                            }}
                        >
                            Удалить
                        </button>
                    </div>
                </button>
            </li>
        {/each}
    </ul>
</main>

<style lang="scss">
    main {
        border-radius: 35px;
        flex: 1;
        background-color: var(--white);
        padding: 35px;

        .btn-add {
            display: flex;
            gap: 4px;
            flex-direction: column;
            align-items: end;
            position: absolute;
            right: 40px;
            top: 20px;

            button {
                background-color: var(--dark-blue-40);
                padding: 6px;
                width: max-content;
                border-radius: 8px;
                font-size: 14px;
            }
        }

        .hidden {
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

                    img {
                        height: 50px;
                        width: 50px;
                    }
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
    }
</style>
