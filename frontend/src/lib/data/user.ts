import { fetchJSON, fetchPlain } from "$lib/fetch";

export type User = {
    id: number;
    login: string;
    first_name: string;
    last_name: string;
    middle_name: string;
    phone: string;
};

/** Информация о текущем пользователе */
export async function fetchMe(): Promise<User> {
    return (await fetchJSON<User>("/users/me")).data;
}

export async function fetchUsers(): Promise<User[]> {
    return (await fetchJSON<User[]>("/users")).data;
}

export async function deleteUser(id: number): Promise<void> {
    await fetchPlain(`/users/${id}`, { method: "DELETE" });
}
