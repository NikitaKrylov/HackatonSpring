import type { Placement } from "$lib/data/placement";
import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ params, parent }) => {
    let { placements } = await parent();
    const id = Number(params.id);
    let placement = placements.find(x => x.id === id);
    if (placement === undefined) redirect(303, "/map");
    return { placement };
};
