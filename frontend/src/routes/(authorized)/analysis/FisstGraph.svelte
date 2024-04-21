<script lang="ts">
    import Chart from 'chart.js/auto';
    import { onMount } from "svelte";

    let cons = []
    let coords = []

    let ctx: HTMLCanvasElement;
    let labels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    onMount( async () => {
        cons = await fetch('https://hack.clayenkitten.ru/api/algorithms/trend_prediction')
        .then(data => data.json())

        cons[0].map(coord => coords.push(coord[1]))
        coords = coords

        console.log(coords);

        
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                label: '',
                data: coords,
                backgroundColor: [
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(71, 146, 206, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
                    'rgba(181, 211, 235, 1)',
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