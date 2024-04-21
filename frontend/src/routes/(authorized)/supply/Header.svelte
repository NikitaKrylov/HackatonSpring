<script lang="ts">
    import { PUBLIC_BASE_URL } from "$env/static/public";
    import { fetchPlain } from "$lib/fetch";

    async function importFn() {
        let blob = await uploadFile();
        let formData = new FormData();
        formData.append("data", blob);

        fetchPlain("/offers/import", {
            body: formData,
            method: "POST"
        });
    }

    async function uploadFile(): Promise<Blob> {
        const input = document.createElement("input");
        input.type = "file";

        let promise = new Promise<Blob>(resolve => {
            input.onchange = async e => {
                let target = e.target as HTMLInputElement;
                let file = target.files![0];
                resolve(file);
            };
        });
        input.click();

        return promise;
    }
</script>

<header>
    <div class="text">
        <h2>Заявки</h2>
        <p>Следите и удобно управляйте своими заявками на закупки</p>
    </div>
    <div class="btns">
        <button on:click={importFn}>
            <img src="/btn-import.svg" alt="Импорт" />
        </button>
        <a href={`${PUBLIC_BASE_URL}/offers/export`} download>
            <img src="/btn-export.svg" alt="Экспорт" />
        </a>
    </div>
</header>

<style lang="scss">
    header {
        display: flex;
        margin-bottom: 46px;
    }

    h2 {
        font-weight: 700;
        font-size: 30px;
        margin-bottom: 8px;
    }

    p {
        font-weight: 500;
        font-size: 14px;
    }

    .btns {
        display: flex;
        gap: 24px;
        margin-left: auto;
        a, button {
            display: flex;
            height: 65px;
            &:hover {
                filter: brightness(90%);
            }
        }
    }
</style>
