import { browser } from "$app/environment";
import { tokenCookie } from "./auth";
import { PUBLIC_BASE_URL } from "$env/static/public";
import Cookies from "js-cookie";

export async function fetchPlain(endpoint: string, init?: FetchInit): Promise<Response> {
    if (!init) init = {};
    init.headers = new Headers(init.headers);

    addAuthorizationHeader(init.headers);

    const fetchFunc = init.fetch ?? fetch;
    return fetchFunc(PUBLIC_BASE_URL + endpoint, init);
}

export async function fetchJSON<T>(
    endpoint: string,
    init?: FetchInit
): Promise<{ data: T; response: Response }> {
    let promise = fetchPlain(endpoint, init);
    return promise.then(async r => ({
        data: await extractJSON<T>(r),
        response: r
    }));
}

function addAuthorizationHeader(headers: Headers) {
    if (browser) {
        const token = Cookies.get(tokenCookie);
        headers.append("Authorization", "Bearer " + token);
    }
}

function extractJSON<T>(r: Response): PromiseLike<T> {
    return r.json();
}

export type FetchInit = RequestInit & {
    fetch?: typeof fetch;
};
