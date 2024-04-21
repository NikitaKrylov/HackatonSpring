<script lang="ts">
    export let selected; String;
    
</script>

<section>
    <select name="" id="">
        <option selected value="">Молочные продукты</option>
        <option value="">Бакалея</option>
        <option value="">Овощи и фрукты</option>
    </select>
    <select name="" id="">
        <option selected value="">Молоко</option>
        <option value="">Сметана</option>
        <option value="">Творог</option>
    </select>
</section>

<style lang="scss">
    section{
        padding: 12px 10px;
        background-color: var(--dark-blue-10);
        border-radius: 12px;
        display: flex;
        gap: 36px;
    }
</style>