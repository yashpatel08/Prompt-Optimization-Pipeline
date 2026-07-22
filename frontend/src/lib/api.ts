// src/lib/api.ts

const API = process.env.NEXT_PUBLIC_API_URL!;

export async function api<T>(
    endpoint: string,
    options?: RequestInit
): Promise<T> {
    const res = await fetch(`${API}${endpoint}`, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...options?.headers,
        },
    });

    if (!res.ok) {
        throw new Error(await res.text());
    }

    return res.json();
}