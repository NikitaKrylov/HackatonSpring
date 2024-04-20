import { goto } from "$app/navigation";
import { PUBLIC_BASE_URL } from "$env/static/public";

/** Name of the token cookie */
export const tokenCookie = "token52";

/** Only call on the browser! */
export function setTokenCookie(token: string) {
    var datetime = new Date();
    var time = datetime.getTime();
    var expireTime = time + 1000 * 36000;
    datetime.setTime(expireTime);
    document.cookie = `${tokenCookie}=${token}; SameSite=Lax; Secure; expires=${datetime.toUTCString()}+';path=/`;
}

export async function login(email: string, password: string): Promise<string> {
    const url = `${PUBLIC_BASE_URL}/users/login`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({ username: email, password })
    });
    if (response.ok) {
        const data: { access_token: string } = await response.json();
        return data.access_token;
    } else {
        throw new Error("Запрос логина провалился");
    }
}

export async function logout() {
    document.cookie = tokenCookie + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
    await goto("/signin");
}
