<script lang="ts"></script>

<div class="card">
    <h3>Склад 1</h3>
    <div class="busy">
        <p>Загруженность</p>
        <div class="busy-blocks">
            <p class:active={true}>
            <p class:active={false}>
            <p class:active={false} >
        </div>
    </div>
    <p>Обработал 20 заявок на прошлой неделе</p>
</div>

<style lang="scss">
    .card{
        max-width: 236px;
        background: rgba(228, 248, 230, 1);
        border-radius: 35px;
        text-align: center;
        padding: 26px 7px 20px;
    }

    h3 {
        font-size: 26px;
        margin-bottom: 20px;
    }

    p{
        display: inline-block;
    }

    .busy {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 18px;

        .busy-blocks {
            display: flex;
            align-items:center;
            gap: 4px;

            p{
                width: 17px;
                height: 6px;
                background-color: rgba(172, 210, 255, 1);

                &:first-child{
                    border-radius: 4px 0 0 4px;
                }

                &:last-child{
                    border-radius: 0 4px 4px 0;
                }

                &.active {
                    background-color: rgba(54, 207, 29, 1);
                }
            }
        }
    }
</style>