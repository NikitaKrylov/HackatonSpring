<script lang="ts">
    import Busy from "$lib/components/Busy.svelte";
</script>

<div class="card">
    <h3>Склад 1</h3>
    <div class="busy">
        <p>Загруженность</p>
        <Busy/>
    </div>
    <p>Обработал 20 заявок на прошлой неделе</p>
</div>

<style lang="scss">
    .card{
        font-size: 0.875;
        max-width: 14rem;
        background: rgba(228, 248, 230, 1);
        border-radius: 35px;
        text-align: center;
        padding: 20px 7px 16px;
    }

    h3 {
        font-size: 1.2rem;
        margin-bottom: 0.625rem;
    }

    p{
        display: inline-block;
    }

    .busy {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 18px;
        margin-bottom: 0.625rem;
        
    }
</style>