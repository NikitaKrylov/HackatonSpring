import { fetchPlacements } from "$lib/data/placement";
import { fetchProducts } from "$lib/data/product";
import { fetchSupplies } from "$lib/data/supply";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async () => {
    const placements = await fetchPlacements();
    const supplies = await fetchSupplies();
    const products = await fetchProducts();
    return { placements, supplies, products };
};
