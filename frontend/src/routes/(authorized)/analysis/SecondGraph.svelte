<script lang="ts">
    import Chart from 'chart.js/auto';
    import { onMount } from "svelte";

    let ctx: HTMLCanvasElement;
    let labels = [10, 20, 30, 40, 50, 60, 70]

    onMount( async () => {
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: '',
                    data: [65, 59, 80, 81, 56, 55, 40],
                    fill: false,
                    borderColor: 'rgba(71, 146, 206, 1)',
                    tension: 0.1
                }]
            }
        });
    });

</script>

<h4>Тренды</h4>
<canvas id="myChart" bind:this={ctx}></canvas>

<style lang="scss">
    h4{
        font-weight: 700;
        font-size: 22px;
        margin-bottom: 20px;
    }

    #myChart{
        max-height: 500px;
    }
    
</style>