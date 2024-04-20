<script lang="ts">
    import Chart from 'chart.js/auto';
    import { onMount } from "svelte";

    let ctx: HTMLCanvasElement;
    let labels = [10, 20, 30, 40, 50, 60, 70]

    onMount( async () => {
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                label: '',
                data: [65, 59, 80, 81, 56, 55, 40],
                backgroundColor: [
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                ],
                barPercentage: 0.5,
                }]
            }
        });
    });

</script>

<h4>Прогнозирование  объемов продаж</h4>
<canvas id="myChart" bind:this={ctx}></canvas>

<style lang="scss">
    h4{
        font-weight: 700;
        font-size: 22px;
        margin-bottom: 20px;
    }

    #myChart{
        max-height: 220px;
    }
    
</style>