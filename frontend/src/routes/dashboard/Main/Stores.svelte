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
        max-width: 734px;
        text-align: right;

        button {
            color: var(--egg-blue-100);
            position: relative;
            margin-bottom: 16px;

            &::after{
                content: '';
                position: absolute;
                display: inline-block;
                background-image: url('/icons/arrow-right.svg');
                background-repeat: no-repeat;
                width: 7px;
                height: 14px;
                right: -15px;
                top: 4px;
            }
        }

        .stores{
            display: flex;
            justify-content: space-between;
        }
    }
</style>