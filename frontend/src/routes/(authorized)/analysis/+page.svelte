<script lang="ts">
    import Filter from './Filter.svelte';
    import FisstGraph from './FisstGraph.svelte';
    import SecondGraph from './SecondGraph.svelte';
    import ThirdGraph from './ThirdGraph.svelte';
</script>

<main>
    <header>
        <h2>Аналитика</h2>
        <p>Следите за тенденциями и различной информацией по вашим товарам</p>
    </header>

    <div class="filters">
        <Filter/>
        <Filter/>
    </div>

    <div class="firstGraph">
        <FisstGraph/>
    </div>
    <div class="listGraphics">
        <section>
            <SecondGraph/>
        </section>
        <section>
            <ThirdGraph/>
        </section>
    </div>

</main>

<style lang="scss">
    main{
        flex: 1;
        background-color: var(--white);
        padding: 35px;
        border-radius:35px;

        header{
            margin-bottom: 46px;
            font-weight: 500;
            font-size: 14px;

            h2{
                font-weight: 700;
                font-size: 30px;
                margin-bottom: 8px;
            }
        }

        .filters{
            display: flex;
            max-width: 432px;
            gap: 22px;
            margin-bottom: 42px;
        }

        .firstGraph{
            padding: 32px;
            border-radius: 35px;
            background-color: var(--dark-blue-10);

        }

        .listGraphics{
            display: flex;
            justify-content: space-between;
            gap: 18px;
            margin-top: 18px;

            section{
                border-radius: 35px;
                background-color: var(--dark-blue-10);
                padding: 32px;
                min-width: 500px;
            }
        }
    }
</style>