<script lang="ts">
    export let status: string;
    const color: Record<string, string> = {
        "В обработке": "#FFF9E5",
        Активный: "#D2E9FD",
        Отменен: "#FFD7D7",
        Выполнен: "#C6EEDE"
    };
</script>

<span style:background-color={color[status]}>{status}</span>

<style lang="scss">
    span {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 20px;
        font-size: 14px;
    }
</style>
