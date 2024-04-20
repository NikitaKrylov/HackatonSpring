import { fetchJSON } from "$lib/fetch";

export interface Placement {
    id: number;
    name: string;
    address: string;
    coord: [number, number];
    placement_type: "storage" | "client";
    workload: number;
    capacity: number;
}

export async function fetchPlacements(): Promise<Placement[]> {
    return fetchJSON<Placement[]>("/placements").then(x => x.data);
}
