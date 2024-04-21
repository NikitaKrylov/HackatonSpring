<script lang="ts">
    import Chart from 'chart.js/auto';
    import { onMount } from "svelte";
    
    let cons = []
    let coords = []

    let ctx: HTMLCanvasElement;
    let labels = [1,2,3,4,8,9,10,11,12,13,14,19,20,21,22,23,27,28,34,35,36,37,38,39,40,41,46,47,48,49,50,51,52,]

    onMount( async () => {

        cons = await fetch('https://hack.clayenkitten.ru/api/algorithms/trend_prediction')
        .then(data => data.json())

        cons[1].map(coord => coords.push(coord[1]))
        coords = coords

        console.log(coords);

        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: '',
                    data: coords,
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