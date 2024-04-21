import { fetchJSON, fetchPlain } from "$lib/fetch";
import type { Role } from "./role";

export type User = {
    id: number;
    login: string;
    first_name: string;
    last_name: string;
    middle_name: string;
    phone: string;
    role: Role;
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

export async function setUserRole(user: number, role: number) {
    await fetchPlain("/users/roles", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify([{ id: user, role_id: role }])
    });
}
