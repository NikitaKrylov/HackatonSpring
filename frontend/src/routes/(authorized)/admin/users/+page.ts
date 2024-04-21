import { fetchUsers } from "$lib/data/user";
import type { PageLoad } from "./$types";

export const load: PageLoad = async () => {
    return {
        users: await fetchUsers()
    };
};
