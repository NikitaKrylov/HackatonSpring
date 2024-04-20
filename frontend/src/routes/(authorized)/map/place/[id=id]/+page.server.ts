import type { Place } from "$lib";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ params }) => {
    const id = Number(params.id);
    const place: Place = {
        id,
        name: "Склад 1",
        address: "Улица Шишкина",
        place_kind: "warehouse",
        workload: 2,
        products: 10
    };
    return { place };
};
