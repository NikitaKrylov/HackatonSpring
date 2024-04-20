<script lang="ts">
    export let name;
    export let tasks;
    $: console.log(tasks)
</script>

<section>
    <h4>{name}</h4>
    <ul>
        {#each tasks as task}
            <li>{task}</li>
        {/each}
    </ul>
</section>

<style lang="scss">
    section{
        max-width: 17.3rem;

        background-color: var(--egg-blue-60);
        border-radius: 35px;
        padding: 30px;

        display: flex;
        flex-direction: column;
        justify-content: space-between;

        h4{
            font-weight: 700;
            font-size: 22px;
            margin-bottom: 22px;
        }

        ul {
            font-weight: 500;
            font-size: .8rem;
            border-top: 1px solid var(--dark-blue-50);
            padding-top: 22px;

            li{
                list-style: inside;
                color: var(--dark-blue-70);

                &:not(:last-child){
                    margin-bottom: 16px;
                }
            }

            
        }
    }
</style>