// @ts-nocheck
import { get } from 'svelte/store';
import { authStore } from './stores.js';  // lo crearemos justo abajo

const API = import.meta.env.VITE_API_BASE_URL;

/** Wrapper para llamar a tu API con Authorization automática */
export async function apiFetch(path, options = {}) {
  const url = `${API}${path}`;
  const token = get(authStore).accessToken;

  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {})
  };

  const res = await fetch(url, {
    credentials: 'include',  // si decides usar cookies
    ...options,
    headers: {
      ...headers,
      ...options.headers
    }
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || res.statusText);
  }

  return res.json();
}
