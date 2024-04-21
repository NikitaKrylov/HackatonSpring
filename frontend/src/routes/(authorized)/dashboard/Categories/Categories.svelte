<script lang="ts">
    import Chart from "chart.js/auto";
    import { onMount } from "svelte";

    let items = async () => {
        return await fetch(
            "https://hack.clayenkitten.ru/api/purchases/statistic?category=Овощи"
        ).then(data => data.json());
    };
    let ctx: HTMLCanvasElement;

    onMount(async () => {
        let response = await items();
        const arr = [];
        const names = [];

        for (let key in response.categories) {
            names.push(key);
            arr.push(response.categories[key]);
        }

        var myChart = new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: names,
                datasets: [
                    {
                        data: arr,
                        backgroundColor: [
                            "rgba(163, 200, 230, 1)",
                            "rgba(163, 200, 230, 1)",
                            "rgba(145, 190, 226, 1)",
                            "rgba(71, 146, 206, 1)",
                            "rgba(204, 188, 246, 1)",
                            " rgba(177, 155, 242, 1)",
                            "rgba(114, 204, 253, 1)",
                            "rgba(206, 233, 255, 1)"
                        ],
                        hoverOffset: 4
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: "bottom"
                    },
                    title: {
                        display: false,
                        text: ""
                    }
                }
            }
        });
    });
</script>

<section>
    <h3>Категории товаров</h3>
    <p>На диаграмме представлены отношения категорий проданных товаров друг к другу</p>
    <div>
        <canvas id="myChart" bind:this={ctx}></canvas>
    </div>
</section>

<style lang="scss">
    section {
        text-align: center;
        flex: 1;
        background-color: var(--dark-blue-10);
        border-radius: 35px;
        padding: 22px;

        h3 {
            font-weight: 700;
            font-size: 26px;
            line-height: 31px;
            margin-bottom: 18px;
        }

        p {
            margin-bottom: 24px;
        }

        div {
            margin: 0 auto 18px;
            width: 285px;
        }
    }
</style>
