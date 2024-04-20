<script lang="ts">
    import LeftBlock from "./LeftBlock.svelte";
    import RightBlock from "./RightBlock.svelte";

</script>

<main>
    <LeftBlock/>
    <RightBlock/>
</main>

<style lang="scss">
    main{
        margin-top: 18px;
        max-width: 724px;
        padding: 22px;
        border: 1px solid var(--dark-blue-50);
        border-radius: 35px;

        display: flex;
        justify-content: space-between;
    }
</style>