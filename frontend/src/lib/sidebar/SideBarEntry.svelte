<script lang="ts">
    import { page } from "$app/stores";

    export let icon: string;
    export let path: string;
    export let name: string;
</script>

<a class:active={$page.url.pathname.startsWith(path)} href={path}>
    <slot>
        <img src={`/icons/${icon}.svg`} alt="" />
        <span>{name}</span>
    </slot>
</a>

<style lang="scss">
    a {
        display: flex;
        text-align: center;
        gap: 18px;
        color: var(--dark-blue-90);
        padding: 12px 16px;
        text-decoration: none;

        &.active {
            background-color: var(--egg-blue-100);
            border-radius: 15px;
            color: var(--white);
            img {
                filter: invert(100%);
            }
        }
    }
</style>
