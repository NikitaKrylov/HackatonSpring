import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ params, parent }) => {
    const { supplies, placements } = await parent();
    const id = Number(params.id);
    const supply = supplies.find(x => x.id === id);
    if (supply === undefined) redirect(303, "/map");
    return { supply, placements };
};
