import { fetchJSON } from "$lib/fetch";

export type Role = {
    id: number;
    name: string;
    is_admin: boolean;
}

export async function fetchRoles(): Promise<Role[]> {
    return (await fetchJSON<Role[]>("/roles")).data;
}
