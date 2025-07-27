<script lang="ts">
// @ts-nocheck
import Section from '$lib/components/Section.svelte';
import { apiFetch } from '$lib/api';
import { authStore } from '$lib/stores';
import { goto } from '$app/navigation';

// Datos del formulario
let username = '';
let password = '';
let errorMsg = '';

async function handleLogin() {
  errorMsg = '';
  try {
    const data = await apiFetch('/login/', {
      method: 'POST',
      body: JSON.stringify({ username, password })
    });
    // Guardar tokens en el store y redirigir
    authStore.login({ access: data.access, refresh: data.refresh, user: null });
    goto('/catalog');
  } catch (e) {
    errorMsg = e.message;
  }
}
</script>

<!-- Section: Design Block -->
<section class="background-radial-gradient overflow-hidden">
  <style>
    .background-radial-gradient {
      background-color: hsl(220, 60%, 10%);
      background-image:
        radial-gradient(650px circle at 0% 0%, #23123a 25%, #005080 45%, #a13a4a 70%, #b82030 90%, transparent 100%),
        radial-gradient(1250px circle at 100% 100%, #005080 20%, #23123a 50%, #a13a4a 75%, #b82030 90%, transparent 100%);
    }
    #radius-shape-1 { height:220px; width:220px; top:-60px; left:-130px; background: radial-gradient(#23123a,#b82030); }
    #radius-shape-2 { border-radius:38% 62% 63% 37%/70% 33% 67% 30%; bottom:-60px; right:-110px; width:300px; height:300px; background:radial-gradient(#005080,#a13a4a); }
    .bg-glass { background-color: hsla(0,0%,100%,0.85)!important; backdrop-filter: saturate(200%) blur(25px); }
  </style>

  <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
    <div class="row gx-lg-5 align-items-center mb-5">
      <!-- Texto de bienvenida -->
      <div class="col-lg-6 mb-5 mb-lg-0" style="z-index:10">
        <h1 class="my-5 display-5 fw-bold ls-tight" style="color: hsl(218,81%,95%)">
          Administración<br/>
          <span style="color: hsl(218,81%,75%)">JLF Materiales Eléctricos</span>
        </h1>
        <p class="mb-4 opacity-70" style="color: hsl(218,81%,85%)">
          Bienvenido al panel de administración de <strong>JLF Materiales Eléctricos</strong>...
        </p>
      </div>

      <!-- Formulario -->
      <div class="col-lg-6 mb-5 mb-lg-0 position-relative">
        <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
        <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>
        <div class="card bg-glass">
          <div class="card-body px-4 py-5 px-md-5">
            <form on:submit|preventDefault={handleLogin}>
              <h2 class="mb-4">Login</h2>

              {#if errorMsg}
                <div class="alert alert-danger" role="alert">{errorMsg}</div>
              {/if}

              <!-- Username -->
              <div class="form-outline mb-4">
                <input
                  bind:value={username}
                  type="text"
                  id="username"
                  class="form-control"
                  required
                />
                <label class="form-label" for="username">Nombre de usuario</label>
              </div>

              <!-- Password -->
              <div class="form-outline mb-4">
                <input
                  bind:value={password}
                  type="password"
                  id="password"
                  class="form-control"
                  required
                />
                <label class="form-label" for="password">Contraseña</label>
              </div>

              <!-- Submit -->
              <button
                type="submit"
                class="btn btn-primary btn-block mb-4"
              >
                Iniciar sesión
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
