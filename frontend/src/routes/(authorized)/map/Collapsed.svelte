<script lang="ts">
    import { createEventDispatcher } from "svelte";

    let dispatch = createEventDispatcher<{ expand: void }>();
</script>

<section>
    <button on:click={() => dispatch("expand")}>
        <img src="/icons/collapse.svg" alt="Раскрыть" />
    </button>
</section>

<style lang="scss">
    section {
        position: absolute;
        right: 0;
        top: 0;
        height: 100%;
        background-color: white;
        border-radius: 25px;
        padding: 22px;
    }
    button {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 28px;
        height: 28px;
        img {
            transform: scaleX(-1);
        }
    }
</style>
