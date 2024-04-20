import { fetchPlacements } from "$lib/data/placement";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async () => {
    const placements = await fetchPlacements();
    return { placements };
};
