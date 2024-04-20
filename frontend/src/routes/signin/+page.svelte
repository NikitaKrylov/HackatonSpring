<script lang="ts">
    import { goto } from "$app/navigation";
    import { login, setTokenCookie } from "$lib/auth";

    let email: string;
    let password: string;

    const click = async () => {
        const token = await login(email, password);
        setTokenCookie(token);
        await goto("/dashboard");
    };
</script>

<main>
    <form>
        <img src="/logo.png" alt="" />
        <h1>Вход в аккаунт</h1>
        <label>
            <span>Email</span>
            <input bind:value={email} type="email" />
        </label>
        <label>
            <span>Пароль</span>
            <input bind:value={password} type="password" />
        </label>
        <button type="button" on:click={click}>Войти</button>
    </form>
</main>

<style lang="scss">
    main {
        display: flex;
        height: 100%;
        justify-content: center;
        align-items: center;
        background-color: var(--dark-blue-20);
    }
    form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: stretch;
        width: 516px;

        border-radius: 25px;
        padding: 76px 52px 52px 52px;
        background-color: var(--white);

        img {
            width: 200px;
            align-self: center;
        }
        h1 {
            color: var(--dark-blue-90);
            font-size: 30px;
            font-weight: 700;
            margin: 46px 0;
            text-align: center;
        }
        label {
            display: flex;
            flex-direction: column;
            gap: 8px;
            & ~ label {
                margin-top: 16px;
            }

            span {
                color: var(--dark-blue-90);
                font-size: 14px;
            }
            input {
                border: 1px solid var(--dark-blue-50);
                border-radius: 10px;
                padding: 12px 16px;
            }
        }
        button {
            padding: 12px 16px;
            margin-top: 60px;

            color: var(--white);
            background-color: var(--egg-blue-100);
            font-size: 22px;
            font-weight: 700;
            border-radius: 10px;
        }
    }
</style>
