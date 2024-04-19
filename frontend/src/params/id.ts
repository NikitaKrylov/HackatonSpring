import type { ParamMatcher } from "@sveltejs/kit";

export const match: ParamMatcher = param => {
    const id = Number(param);
    return Number.isInteger(id) && id >= 0;
};
