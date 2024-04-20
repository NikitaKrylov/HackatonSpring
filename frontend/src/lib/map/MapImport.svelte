<script lang="ts">
    import { PUBLIC_MAP_KEY } from "$env/static/public";

    $: api_src = `https://api-maps.yandex.ru/v3/?apikey=${PUBLIC_MAP_KEY}&lang=ru_RU`;
</script>

<svelte:head>
    <script src={api_src}></script>
</svelte:head>
