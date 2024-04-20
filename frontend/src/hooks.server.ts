import { tokenCookie } from "$lib/auth";
import { redirect, type Handle } from "@sveltejs/kit";
export const handle: Handle = async ({ event, resolve }) => {
    const authorized_path = !event.url.pathname.startsWith("/signin");
    const admin_path = event.url.pathname.startsWith("/admin");

    // TODO: validate token
    const user_authorized = !!event.cookies.get(tokenCookie);
    // TODO: check content of JWT
    const user_admin = false;

    if (authorized_path && !user_authorized) redirect(307, "/signin");
    if (!authorized_path && user_authorized) redirect(307, "/dashboard");
    if (admin_path && !user_admin) redirect(307, "/dashboard");

    const response = await resolve(event);
    return response;
};
