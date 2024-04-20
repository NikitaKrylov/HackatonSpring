<script lang="ts">
    export let status: string;
    const color: Record<string, string> = {
        Ожидает: "#FFF9E5",
        "В работе": "#D2E9FD",
        Отменено: "#FFD7D7",
        Завершено: "#C6EEDE"
    };
</script>

<span style:background-color={color[status]}>{status}</span>

<style lang="scss">
    span {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 20px;
    }
</style>
