<script lang="ts">
    import Chart from 'chart.js/auto';
    import { onMount } from "svelte";

    let ctx: HTMLCanvasElement;
    let labels = [
        'Red',
        'Blue',
        'Yellow',
        
    ]

    onMount( async () => {
        var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'My First Dataset',
                data: [65, 59, 80, 81, 56, 55, 40],
                backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    });

</script>

<div>
    <p class="text">
        <p>Категория <span>+12,6%</span></p>
        <select name="" id="">
            <option selected value="">Молочные продукты</option>
        </select>
    
    <canvas id="myChart" bind:this={ctx}></canvas>
</div>

<style lang="scss">
    div {
        width: 280px;

        .text{
            display: flex;
            justify-content: space-between;
            
            p{
                font-weight: 600;
                font-size: 22px;

                span{
                    color: rgba(54, 207, 29, 1);
                }
            }
        }
    }
</style>