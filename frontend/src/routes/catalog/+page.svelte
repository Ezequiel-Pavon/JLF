<script lang="ts">
// @ts-nocheck
  import Section from '$lib/components/Section.svelte';
  import { apiFetch } from '$lib/api';
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { writable, derived, get } from 'svelte/store';
  import { authStore } from '$lib/stores';

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
  let formError = '';

  async function submitForm() {
    formError = '';
    try {
      const newProd = {
        slug,
        name,
        category,
        description,
        images: imagesInput.split(',').map(s => s.trim()).filter(s => s),
        features: featuresInput.split(',').map(s => s.trim()).filter(s => s)
      };
      const created = await apiFetch('/products/', {
        method: 'POST',
        body: JSON.stringify(newProd)
      });
      products.update(list => [created, ...list]);
      // reset form
      slug = name = category = description = imagesInput = featuresInput = '';
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
                Imágenes (URLs separadas por coma)
              </label>
              <input
                id="images"
                class="form-control"
                bind:value={imagesInput}
                placeholder="/img/a.jpg, /img/b.jpg"
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
      <div class="col-lg-3 col-md-4 col-6 mb-4">
        <!-- svelte-ignore a11y-no-redundant-roles -->
        <button
          type="button"
          role="button"
          tabindex="0"
          class="card catalog-card h-100 text-start { $selectedSlug === prod.slug ? 'expanded' : '' }"
          on:click={() => selectProduct(prod.slug)}
        >
          <img src={prod.images[0] ?? ''} alt={prod.name} class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">{prod.name}</h5>
            {#if $selectedSlug === prod.slug}
              <p class="mt-2">Categoría: {prod.category}</p>
              <p>{prod.description ?? 'Descripción no disponible.'}</p>
              <ul>
                {#each prod.features as f}<li>{f}</li>{/each}
              </ul>
            {/if}
          </div>
        </button>
      </div>
    {/each}

    {#if $filtered.length === 0}
      <div class="col-12">
        <p class="text-center">No se encontraron productos.</p>
      </div>
    {/if}
  </div>
</Section>
