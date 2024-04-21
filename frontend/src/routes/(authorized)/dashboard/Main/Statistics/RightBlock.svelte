<script lang="ts">
    import Chart from 'chart.js/auto';
    import { onMount } from "svelte";

    let ctx: HTMLCanvasElement;
    let labels = [
        '1-10 August',
        '',
        '11-20 August',
        '',
        '21-31 August',
        ''
    ]

    onMount( async () => {
        var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: '',
                data: [65, 59, 80, 81, 56, 55, 40],
                backgroundColor: [
                    'rgba(124, 89, 233, 1)',
                    'rgba(240, 235, 253, 1)',
                    'rgba(124, 89, 233, 1)',
                    'rgba(240, 235, 253, 1)',
                    'rgba(124, 89, 233, 1)',
                    'rgba(240, 235, 253, 1)',
                ],
                borderRadius: [5, 5, 5, 5, 5, 5],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                legend: {
                    display: false,
                },
                title: {
                    display: false,
                    text: ''
                }
            }
        }
    });
    });

</script>

<div>
    <div class="text">
        <p>Категория <span>+12,6%</span></p>
        <select name="" id="">
            <option selected value="">Бакалея</option>
            <option selected value="">Молочные продукты</option>
        </select>
    </div>    
    
    
    <canvas id="myChart" bind:this={ctx}></canvas>
</div>

<style lang="scss">
    div {
        flex: 1;
        max-width: 400px;

        .text{
            display: flex;
            justify-content: space-between;

            p{
            font-weight: 600;
            font-size: 22px;

                span{
                    font-size: 14px;
                    color: rgba(54, 207, 29, 1);
                    margin-left: 4px;
                    margin-right: 4px;
                }
            }

            select option{
                &:focus {
                    border: none;
                }
            }
        }

        
    }
</style>