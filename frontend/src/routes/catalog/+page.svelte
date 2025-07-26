<script lang="ts">
// @ts-nocheck
  import Section from '$lib/components/Section.svelte';
  import { apiFetch } from '$lib/api';
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { writable, derived, get } from 'svelte/store';
  import { authStore } from '$lib/stores';

  // store para el slug que estamos a punto de eliminar
  const deleteSlug = writable<string|null>(null);

  // Función que llama a la API para borrar
  async function deleteProduct(slug: string) {
    try {
      const res = await fetch(
        `${import.meta.env.VITE_API_BASE_URL}/products/${slug}/`,
        {
          method: 'DELETE',
          headers: {
            Authorization: `Bearer ${get(authStore).accessToken}`,
          }
        }
      );
      if (!res.ok) throw new Error(`Error ${res.status}`);
      // Si salió bien, removemos de la lista local
      products.update(list => list.filter(p => p.slug !== slug));
      deleteSlug.set(null);
    } catch (e) {
      alert(`No se pudo eliminar: ${e.message}`);
    }
  }

  function confirmDelete(slug: string) {
    deleteSlug.set(slug);
  }
  function cancelDelete() {
    deleteSlug.set(null);
  }

  // 1) Productos
  const products = writable([]);
  onMount(async () => {
    const datos = await apiFetch('/products/');
    products.set(datos);
  });

  // 2) Categorías derivadas
  const categories = derived(products, ($products) =>
    [...new Set($products.map((p) => p.category))]
  );

  // 3) Búsqueda y filtros
  const search = writable('');
  const selectedCategories = writable(new Set<string>());

  const filtered = derived(
    [products, search, selectedCategories],
    ([$products, $search, $selected]) =>
      $products.filter((p) => {
        const matchesSearch = p.name
          .toLowerCase()
          .includes($search.trim().toLowerCase());
        const matchesCategory =
          $selected.size === 0 || $selected.has(p.category);
        return matchesSearch && matchesCategory;
      })
  );

  // 4) Selección inline
  const selectedSlug = writable<string | null>(null);
  onMount(() => {
    const sel = new URLSearchParams(get(page).url.search).get('select');
    if (sel) selectedSlug.set(sel);
  });
  function toggleCategory(cat: string) {
    selectedCategories.update((s) => {
      const next = new Set(s);
      next.has(cat) ? next.delete(cat) : next.add(cat);
      return next;
    });
  }
  function selectProduct(slug: string) {
    selectedSlug.update((cur) => (cur === slug ? null : slug));
  }

  // 5) Admin?
  const isAdmin = derived(authStore, ($auth) => !!$auth.accessToken);

  // 6) Formulario “Agregar Producto”
  const showForm = writable(false);
  let slug = '';
  let name = '';
  let category = '';
  let description = '';
  let imagesInput = '';
  let featuresInput = '';
  let files: File[] = [];
  let formError = '';

  function handleFiles(event) {
    files = Array.from(event.target.files);
  }

  async function submitForm() {
    formError = '';
    try {
      const fd = new FormData();
      fd.append('slug', slug);
      fd.append('name', name);
      fd.append('category', category);
      fd.append('description', description);
      fd.append('features', JSON.stringify(
        featuresInput.split(',').map(s => s.trim()).filter(s => s)
      ));
      files.forEach((file) => fd.append('images', file, file.name));

      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/products/`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${get(authStore).accessToken}`
        },
        body: fd
      });

      if (!res.ok) {
        // Leer la respuesta JSON con los errores de validación
        const err = await res.json();
        console.error('API Validation Errors:', err);
        formError = JSON.stringify(err, null, 2);
        return;
      }

      const created = await res.json();
      products.update(list => [created, ...list]);
      // reset form...
      showForm.set(false);
    } catch (e) {
      formError = e.message;
    }
  }
</script>

<Section title="Catálogo de Productos" classId="catalog">
  {#if $isAdmin}
    <div class="mb-3 text-end">
      <button
        class="btn btn-success"
        on:click={() => showForm.update(v => !v)}
      >
        {#if $showForm}✖ Cancelar{:else}+ Agregar Producto{/if}
      </button>
    </div>

    {#if $showForm}
      <div class="card mb-4">
        <div class="card-body">
          {#if formError}
            <div class="alert alert-danger">{formError}</div>
          {/if}
          <div class="row g-3">
            <!-- Slug -->
            <div class="col-md-4">
              <label for="slug" class="form-label">Slug</label>
              <input
                id="slug"
                class="form-control"
                bind:value={slug}
                placeholder="p.ej. producto-uno"
              />
            </div>

            <!-- Nombre -->
            <div class="col-md-4">
              <label for="name" class="form-label">Nombre</label>
              <input
                id="name"
                class="form-control"
                bind:value={name}
                placeholder="Nombre del producto"
              />
            </div>

            <!-- Categoría -->
            <div class="col-md-4">
              <label for="category" class="form-label">Categoría</label>
              <input
                id="category"
                class="form-control"
                bind:value={category}
                placeholder="Categoría"
              />
            </div>

            <!-- Descripción -->
            <div class="col-12">
              <label for="description" class="form-label">Descripción</label>
              <textarea
                id="description"
                class="form-control"
                bind:value={description}
                rows="2"
              />
            </div>

            <!-- Imágenes -->
            <div class="col-md-6">
              <label for="images" class="form-label">
                Imágenes (selecciona múltiples archivos)
              </label>
              <input
                id="images"
                type="file"
                multiple
                class="form-control"
                on:change={handleFiles}
              />
            </div>

            <!-- Features -->
            <div class="col-md-6">
              <label for="features" class="form-label">
                Features (separados por coma)
              </label>
              <input
                id="features"
                class="form-control"
                bind:value={featuresInput}
                placeholder="Carac1, Carac2, ..."
              />
            </div>

            <!-- Botón enviar -->
            <div class="col-12 text-end">
              <button class="btn btn-primary" on:click={submitForm}>
                Guardar Producto
              </button>
            </div>
          </div>
        </div>
      </div>
    {/if}
  {/if}

  <!-- Búsqueda y filtros -->
  <div class="row mb-4">
    <div class="col-md-6 mb-3">
      <input
        type="text"
        class="form-control"
        placeholder="Buscar producto..."
        on:input={(e) => search.set(e.target.value)}
      />
    </div>
    <div class="col-md-6 mb-3">
      <div class="d-flex flex-wrap gap-2">
        {#each $categories as cat}
          <button
            type="button"
            class="btn btn-outline-primary btn-sm"
            class:selected={$selectedCategories.has(cat)}
            on:click={() => toggleCategory(cat)}
          >
            {cat}
          </button>
        {/each}
      </div>
    </div>
  </div>

  <!-- Grid de productos -->
  <div class="row">
    {#each $filtered as prod}
      <div class="col-lg-3 col-md-4 col-6 mb-4 position-relative">
        <div class="card catalog-card h-100 text-start { $selectedSlug === prod.slug ? 'expanded' : '' }">
          <!-- Botón de eliminar en esquina -->
          <button
            class="btn btn-sm btn-outline-danger position-absolute"
            style="top: 0.5rem; right: 0.5rem; z-index:10;"
            on:click={() => confirmDelete(prod.slug)}
          >
            🗑
          </button>

          {#if $deleteSlug === prod.slug}
            <!-- Capa de confirmación -->
            <div class="position-absolute w-100 h-100 d-flex flex-column justify-content-center align-items-center bg-white bg-opacity-75" style="z-index:20; top:0; left:0;">
              <p>¿Eliminar <strong>{prod.name}</strong>?</p>
              <div class="d-flex gap-2">
                <button class="btn btn-sm btn-danger" on:click={() => deleteProduct(prod.slug)}>Sí</button>
                <button class="btn btn-sm btn-secondary" on:click={cancelDelete}>No</button>
              </div>
            </div>
          {/if}

          <!-- Resto de la tarjeta -->
          <!-- svelte-ignore a11y-no-redundant-roles -->
          <button
            type="button"
            role="button"
            tabindex="0"
            class="card-body-wrapper h-100"
            on:click={() => selectProduct(prod.slug)}
          >
            <img
              src={prod.images?.[0] ?? '/img/placeholder.png'}
              alt={prod.name}
              class="card-img-top"
            />
            <div class="card-body">
              <h5 class="card-title">{prod.name}</h5>
              {#if $selectedSlug === prod.slug}
                <p class="mt-2">Categoría: {prod.category}</p>
                <p>{prod.description ?? 'Descripción no disponible.'}</p>
                <a href="/contact" class="btn btn-primary btn-sm mt-2">Contactar</a>
              {/if}
            </div>
          </button>
        </div>
      </div>
    {/each}

    {#if $filtered.length === 0}
      <div class="col-12">
        <p class="text-center">No se encontraron productos.</p>
      </div>
    {/if}
  </div>
</Section>

<style>
  .card-body-wrapper {
    display: block;
    text-align: left;
    border: none;
    background: transparent;
    width: 100%;
    height: 100%;
    padding: 0;
  }
  .position-relative { position: relative; }
  .position-absolute { position: absolute; }
</style>
