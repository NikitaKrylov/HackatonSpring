<script lang="ts">
</script>

<section>
    <p>Персональная информация</p>
    <div class="info">
        <ul>
            <li>
                <p>Фамилия</p>
                <p>Тычинин</p>
            </li>
            <li>
                <p>Имя</p>
                <p>Андрей</p>
            </li>
            <li>
                <p>Отчество</p>
                <p>Алсексеевич</p>
            </li>
            <li>
                <p>Телефон</p>
                <p>+7 (952) 821 00 00</p>
            </li>
            <li>
                <p>Почта</p>
                <p>yyyoner@gmail.com</p>
            </li>
            <li >
                <p>Номер сотрудника</p>
                <div class="copy">
                    <p class="num-employee">52000001</p>
                    <button >
                        <img src="/icons/copy.svg" alt="">
                    </button>
                </div>
            </li>
        </ul>
    </div>
    <button class="exit">Выйти из аккаунта</button>
</section>

<style lang="scss">
    section{

        padding-left: 22px;
        padding-top: 60px;

        > p{
            font-weight: 700;
            font-size: 22px;
            margin-bottom: 40px;
        }

        .info{
            max-width: fit-content;
            min-height: fit-content;

            ul {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                row-gap: 40px;
                column-gap: 150px;

                li{
                    max-width: fit-content;
                    
                    p{
                        &:first-child{
                            font-weight: 400;
                            font-size: 14px;
                            color: var(--dark-blue-60);
                            margin-bottom: 6px;
                        }

                        &:last-child{
                            font-weight: 405000;
                            font-size: 16px;
                            max-width: fit-content;
                        }
                    }

                    .copy {
                        display: flex;
                        gap: 8px;
                    }
                }
            }
        }

        .exit {
            margin-top: 50px;
            margin-left: 15px;
            color: rgba(243, 87, 87, 1);
            position: relative;

            &::after{
                content: '';
                position: absolute;
                display: inline-block;
                width: 25px;
                height: 25px;
                background-image: url('/icons/exit_account.svg');
                background-repeat: no-repeat;
                left: -34px;
                top: -4px;

            }
        }
    }
</style>