import { fetchRoles } from "$lib/data/role";
import { fetchUsers } from "$lib/data/user";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    return {
        users: await fetchUsers(),
        roles: await fetchRoles()
    };
};
