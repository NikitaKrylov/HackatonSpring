import { fetchOffers } from "$lib/data/offer";
import { fetchPlacements } from "$lib/data/placement";
import type { PageLoad } from "./$types";

export const load: PageLoad = async () => {
    return {
        placements: await fetchPlacements(),
        offers: await fetchOffers()
    };
};
