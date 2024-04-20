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
