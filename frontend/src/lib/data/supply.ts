import { fetchJSON } from "$lib/fetch";

export type Supply = {
    id: number;
    storage_id: number;
    offers: {
        id: number;
        product_count: number;
        product_id: number;
        placement_id: number;
        supply_id: number;
    }[];
    storage: {
        id: number;
        address: string;
        name: string;
        coord: string;
        placement_type: string;
    };
    created_at: string;
    supply_status: string;
    transport_date: string;
};

export async function fetchSupplies(): Promise<Supply[]> {
    return fetchJSON<Supply[]>("/supplies").then(x => x.data);
}
