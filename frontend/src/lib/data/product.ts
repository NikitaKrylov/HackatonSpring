import { fetchJSON } from "$lib/fetch";

export type Product = {
    id: number;
    sku: number;
    name: string;
    manufactor: string;
    product_measure: string;
    product_amount: number;
    product_volume: number;
    manufacture_date: string;
    expiry_date: string;
    category: string;
};

export async function fetchProducts(): Promise<Product[]> {
    return fetchJSON<Product[]>("/products").then(x => x.data);
}
