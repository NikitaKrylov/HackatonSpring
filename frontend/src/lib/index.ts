export type Supply = {
    id: number;
    date: string;
    status: string;
    stops: number;
};

export type Place = {
    id: number;
    name: string;
    place_kind: "warehouse" | "client";
    address: string;
    workload: number;
    products: number;
}
