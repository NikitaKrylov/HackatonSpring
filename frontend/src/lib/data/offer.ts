import { fetchJSON } from "$lib/fetch";
import type { Placement } from "./placement";
import type { Product } from "./product";

export type Offer = {
    id: number;
    product_count: number;
    product_id: number;
    placement_id: number;
    supply_id: number;
    product: Product;
    placement: Placement;
};

export async function fetchOffers(): Promise<Offer[]> {
    return fetchJSON<Offer[]>("/offers").then(x => x.data);
}
