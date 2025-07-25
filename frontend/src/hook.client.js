// @ts-nocheck
import { authStore } from '$lib/stores';

export function handle({ event, resolve }) {
  authStore.init();
  return resolve(event);
}
