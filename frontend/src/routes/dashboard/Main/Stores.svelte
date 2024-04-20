<script lang='ts'>
    import Store from "./Store.svelte";

</script>

<section>
    <button>Смотреть все</button>
    <div class="stores">
        <Store/>
        <Store/>
        <Store/>
    </div>
</section>

<style lang="scss">
    section{
        max-width: 740px;
        text-align: right;

        button {
            color: var(--egg-blue-100);
            position: relative;
            margin-bottom: 16px;
            padding-right: 14px;

            &::after{
                content: '';
                position: absolute;
                display: inline-block;
                background-image: url('/icons/arrow-right.svg');
                background-repeat: no-repeat;
                width: 7px;
                height: 14px;
                right: 0;
                top: 4px;
            }
        }

        .stores{
            display: flex;
            justify-content: space-between;
            gap: 8px;
        }
    }
</style>