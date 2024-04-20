<script lang="ts"></script>

<div>
    <header>
        <h2>Пользователи</h2>
        <p>Создавайте новых пользователей, управляйте ими и их ролями </p>
    </header>
    <button>
        <img src="/icons/add-contact.svg" alt="">
        <p>Добавить пользователя</p>
    </button>
</div>

<style lang="scss">
    div {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    header{
        margin-bottom: 46px;
    }

    h2{
        font-weight: 700;
        font-size: 30px;
        margin-bottom: 8px;
    }
    
    p{
        font-weight: 500;
        font-size: 14px;
    }

    button{
        display: flex;
        gap: 19px;
        
        background-color: var(--egg-blue-100);
        padding: 15px 20px;
        color: var(--white);
        border-radius: 15px;
    }
</style>