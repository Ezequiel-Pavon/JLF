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

<!-- Section: Design Block -->
<section class="background-radial-gradient overflow-hidden">
<style>
    .background-radial-gradient {
      background-color: hsl(220, 60%, 10%);
      background-image: radial-gradient(650px circle at 0% 0%,
          #23123a 25%,      /* azul oscuro más oscuro */
          #005080 45%,      /* azul claro más oscuro */
          #a13a4a 70%,      /* rojo rosado más oscuro */
          #b82030 90%,      /* rojo fuerte más oscuro */
          transparent 100%),
        radial-gradient(1250px circle at 100% 100%,
          #005080 20%,      /* azul claro más oscuro */
          #23123a 50%,      /* azul oscuro más oscuro */
          #a13a4a 75%,      /* rojo más oscuro */
          #b82030 90%,      /* rojo fuerte más oscuro */
          transparent 100%);
    }

    #radius-shape-1 {
      height: 220px;
      width: 220px;
      top: -60px;
      left: -130px;
      background: radial-gradient(#23123a, #b82030);
      overflow: hidden;
    }

    #radius-shape-2 {
      border-radius: 38% 62% 63% 37% / 70% 33% 67% 30%;
      bottom: -60px;
      right: -110px;
      width: 300px;
      height: 300px;
      background: radial-gradient(#005080, #a13a4a);
      overflow: hidden;
    }

    .bg-glass {
      background-color: hsla(0, 0%, 100%, 0.85) !important;
      backdrop-filter: saturate(200%) blur(25px);
    }
</style>
  <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
    <div class="row gx-lg-5 align-items-center mb-5">
      <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10">
        <h1 class="my-5 display-5 fw-bold ls-tight" style="color: hsl(218, 81%, 95%)">Administración<br />
          <span style="color: hsl(218, 81%, 75%)">JLF Materiales Eléctricos</span>
        </h1>
        <p class="mb-4 opacity-70" style="color: hsl(218, 81%, 85%)">
            Bienvenido al panel de administración de <strong>JLF Materiales Eléctricos</strong>.
            Desde aquí puedes gestionar todo lo relacionado con el inventario, productos, proveedores,
            pedidos, clientes y usuarios del sistema. También podrás generar reportes, actualizar
            precios, monitorear el desempeño de ventas y mantener el catálogo actualizado.
            Si tienes alguna duda, consulta la documentación o contacta al soporte técnico.
        </p>
      </div>

      <div class="col-lg-6 mb-5 mb-lg-0 position-relative">
        <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
        <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>

        <div class="card bg-glass">
          <div class="card-body px-4 py-5 px-md-5">
            <form>
              <h2 class="mb-4">Login</h2>
              <!-- Email input -->
              <div data-mdb-input-init class="form-outline mb-4">
                <input type="name" id="form3Example3" class="form-control" />
                <label class="form-label" for="form3Example3">Nombre</label>
              </div>

              <!-- Password input -->
              <div data-mdb-input-init class="form-outline mb-4">
                <input type="password" id="form3Example4" class="form-control" />
                <label class="form-label" for="form3Example4">Contraseña</label>
              </div>

              <!-- Submit button -->
              <button type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4">
                Sign up
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<!-- Section: Design Block -->

