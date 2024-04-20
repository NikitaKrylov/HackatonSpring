<script></script>

<div class="busy-blocks">
    <p class:active={true}>
    <p class:active={false}>
    <p class:active={false} >
</div>

<style lang="scss">
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
</style>