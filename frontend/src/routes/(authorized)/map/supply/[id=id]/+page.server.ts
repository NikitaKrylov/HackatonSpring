import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    return {
        locations: [{ id: 0 }, { id: 1 }]
    };
};
