<script lang="ts"></script>

<section>
    <div class="text">
        <p class="Extrabold">Статистика по категории</p>
        <p class="Regular">Последние 60 дней</p>
    </div>
    <div class="applications">
        <div><span class="num">136 </span>заявок<div class="perc">+12,6%</div></div>
        <p><span>+40</span> по сравнению с предидущим месяцем</p>
    </div>
</section>

<style lang="scss">
    section{
        max-width: 232px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .text p{
        &:first-child{
            font-weight: 600;
            line-height: 26.4px;
        }

        &:last-child{
            color: var(--dark-blue-60);
            font-size: 14px;
            font-weight: 400;
            margin-top: 8px;
        }
    }

    .applications{
        font-size: 22px;
        font-weight: 600;

        .num {
            font-size: 30px;
            font-weight: 800;
        }

        .perc{
            display: inline-block;
            padding: 4px 12px;
            color: rgba(54, 207, 29, 1);
            background-color: rgba(232, 249, 242, 1);
            border-radius: 100px;
            margin-left: 9px;
        }

        p{
            font-size: 14px;
            color: var(--dark-blue-60);

            span {
                color: rgba(54, 207, 29, 1);
            }
        }
    }
</style>