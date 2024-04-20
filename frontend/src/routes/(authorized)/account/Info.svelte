<script lang="ts"></script>

<section>
    <div class="main">
        <img src="/icons/avatar-acc.svg" alt="avatar">
        <div class="text">
            <p>Тычинин Андрей Алексеевич</p>
            <p>Администратор</p>
        </div>
    </div>
    
</section>

<style lang="scss">
    .main {
        display: flex;
        align-items: center;
        gap: 25px;
        margin-top: 50px;

        img {
            border-radius: 50%;
            width: 120px;
        }

        .text p{

            &:first-child{
                font-weight: 700;
                font-size: 26px;
                margin-bottom: 8px;
            }

            &:last-child{
                font-weight: 500;
            }
        }
    }
</style>