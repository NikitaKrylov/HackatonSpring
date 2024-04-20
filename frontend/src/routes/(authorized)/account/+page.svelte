<script lang="ts">
    import Info from "./Info.svelte";
    import PersonalPanel from "./PersonalPanel.svelte";
</script>

<main>
    <header>
        <p>Ваш аккаунт</p>
    </header>
    <Info />
    <PersonalPanel />
</main>

<style lang="scss">
    main {
        flex: 1;
        background-color: var(--white);
        border-radius: 25px;
        padding: 35px;
        header {
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;

            p {
                display: inline;
                font-weight: 700;
                font-size: 30px;
            }
        }
    }
</style>
