<script lang="ts">
    export let current: number;
    export let maximum: number;

    const off = "#acd2ff";
    let color: string;
    $: if (current / maximum > 0.66) {
        color = "#F35757";
    } else if (current / maximum > 0.33) {
        color = "#FFC700";
    } else {
        color = "#36CF1D";
    }
</script>

<div class="busy-blocks">
    <p style:background-color={color}></p>
    <p style:background-color={current / maximum > 0.33 ? color : off} />
    <p style:background-color={current / maximum > 0.66 ? color : off} />
</div>

<style lang="scss">
    .busy-blocks {
        display: flex;
        align-items: center;
        gap: 4px;

        p {
            width: 17px;
            height: 6px;
            background-color: #acd2ff;

            &:first-child {
                border-radius: 4px 0 0 4px;
            }

            &:last-child {
                border-radius: 0 4px 4px 0;
            }
        }
    }
</style>
