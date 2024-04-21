<script lang="ts">
    import Store from "./Store.svelte";

</script>

<section>
    <a class="seealso" href="/map">Смотреть всё</a>
    <div class="stores">
        <!-- TODO -->
        <a href="/map/place/1"><Store /></a>
        <a href="/map/place/2"><Store /></a>
        <a href="/map/place/3"><Store /></a>
    </div>
</section>

<style lang="scss">
    section {
        max-width: 100%;
        text-align: right;

        .seealso {
            display: block;
            color: var(--egg-blue-100);
            position: relative;
            margin-bottom: 16px;
            padding-right: 14px;
            text-decoration: none;

            &::after {
                content: "";
                position: absolute;
                display: inline-block;
                background-image: url("/icons/arrow-right.svg");
                background-repeat: no-repeat;
                width: 7px;
                height: 14px;
                right: 0;
                top: 4px;
            }
        }

        .stores {
            display: flex;
            justify-content: space-between;
            gap: 8px;
        }
    }
</style>
