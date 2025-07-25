// @ts-nocheck
import { writable } from 'svelte/store';

function createAuth() {
  const { subscribe, set, update } = writable({
    accessToken: null,
    refreshToken: null,
    user: null
  });

  return {
    subscribe,
    login: ({ access, refresh, user }) => {
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      set({ accessToken: access, refreshToken: refresh, user });
    },
    logout: () => {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      set({ accessToken: null, refreshToken: null, user: null });
    },
    init: () => {
      const access = localStorage.getItem('accessToken');
      const refresh = localStorage.getItem('refreshToken');
      if (access) set({ accessToken: access, refreshToken: refresh, user: null });
    }
  };
}

export const authStore = createAuth();
