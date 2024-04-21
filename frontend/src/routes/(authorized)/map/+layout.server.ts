import { fetchPlacements } from "$lib/data/placement";
import { fetchSupplies } from "$lib/data/supply";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async () => {
    const placements = await fetchPlacements();
    const supplies = await fetchSupplies();
    return { placements, supplies };
};
