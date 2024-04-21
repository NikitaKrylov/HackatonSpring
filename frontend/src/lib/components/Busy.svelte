<script lang="ts">
    export let current: number;
    export let maximum: number;

    let color: string;
    $: color = getColor(current, maximum)
    const off = "#acd2ff";
</script>

<script lang="ts" context="module">
    export function getColor(cur: number, max: number) {
        if (cur / max > 0.66) {
            return "#F35757";
        } else if (cur / max > 0.33) {
            return "#FFC700";
        } else {
            return "#36CF1D";
        }
    }
    export function getColorBack(cur: number, max: number) {
        if (cur / max > 0.66) {
            return "#FEEEEE";
        } else if (cur / max > 0.33) {
            return "#FFF9E5";
        } else {
            return "#E4F8E6";
        }
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
