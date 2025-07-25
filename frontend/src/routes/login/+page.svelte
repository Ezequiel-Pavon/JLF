<script>
// @ts-nocheck
  import Section from '$lib/components/Section.svelte';
  import { apiFetch } from '$lib/api';
  import { authStore } from '$lib/stores';
  import { goto } from '$app/navigation';

  let username = '', password = '';
  let errorMsg = '';

  async function handleLogin() {
    errorMsg = '';
    try {
      const data = await apiFetch('/login/', {
        method: 'POST',
        body: JSON.stringify({ username, password })
      });
      // DRF Simple JWT devuelve { access, refresh }
      authStore.login({ access: data.access, refresh: data.refresh, user: null });
      goto('/admin/products');
    } catch (e) {
      errorMsg = e.message;
    }
  }
</script>

<Section title="Admin Login" classId="login">
  <div class="login-form">
    {#if errorMsg}<p class="text-danger">{errorMsg}</p>{/if}
    <input type="text" bind:value={username} placeholder="Usuario" />
    <input type="password" bind:value={password} placeholder="Contraseña" />
    <button class="btn btn-primary" on:click={handleLogin}>Entrar</button>
  </div>
</Section>

<style>
.login-form {
  max-width: 400px;
  margin: 2rem auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
