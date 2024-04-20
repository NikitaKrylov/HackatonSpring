<script lang="ts">
    import Info from "./Info.svelte";
    import PersonalPanel from "./PersonalPanel.svelte";

</script>

<main>
    <header>
        <p>Ваш аккаунт</p>
        <button>Редактировать</button>
    </header>
    <Info/>
    <PersonalPanel/>
</main>

<style lang="scss">
    main {
        flex: 1;    
        background-color: var(--white);
        border-radius: 25px;
        padding: 25px;
        header{
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;

            p{
                display: inline;
                font-weight: 700;
                font-size: 30px;
            }

            button{
                font-weight: 500;
                position: relative;
                color: var(--dark-blue-70);

                &::after{
                    content: '';
                    display: inline-block;
                    position: absolute;
                    height: 20px;
                    width: 20px;
                    left: -34px;
                    background-image: url('/icons/pen.svg');
                    background-repeat: no-repeat;
                }
            }
        }
    }
</style>