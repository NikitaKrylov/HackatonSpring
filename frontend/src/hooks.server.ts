import { tokenCookie } from "$lib/auth";
import { redirect, type Handle } from "@sveltejs/kit";
export const handle: Handle = async ({ event, resolve }) => {
    const authorized_path = !event.url.pathname.startsWith("/signin");

    // TODO: validate token
    const user_authorized = !!event.cookies.get(tokenCookie);

    if (authorized_path && !user_authorized) redirect(303, "/signin");
    if (!authorized_path && user_authorized) redirect(303, "/dashboard");

    const response = await resolve(event);
    return response;
};
