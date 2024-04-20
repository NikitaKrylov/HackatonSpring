<script lang="ts"></script>

<div class="card">
    <h3>Склад 1</h3>
    <div class="busy">
        <p>Загруженность</p>
        <div class="busy-blocks">
            <p class:active={false}>
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
        margin-bottom: 20px;
    }

    p{
        display: inline-block;
    }

    .busy-blocks p{
        display: flex;
        gap: 2px;
        display: inline-block;
        width: 17px;
        border-top: 4px solid rgba(172, 210, 255, 1);
    }
</style>