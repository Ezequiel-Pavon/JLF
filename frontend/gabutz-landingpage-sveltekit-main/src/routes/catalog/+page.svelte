<script>
// @ts-nocheck

  import Section from '$lib/components/Section.svelte';
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { writable, derived } from 'svelte/store';
  import { products } from '$lib/data/products.js';

  // Búsqueda y filtros
  const search = writable('');
  const selectedCategories = writable(new Set());
  const categories = [...new Set(products.map(p => p.category))];

  const filtered = derived(
    [search, selectedCategories],
    ([$search, $selected]) =>
      products.filter((p) => {
        const matchesSearch = p.name.toLowerCase().includes($search.trim().toLowerCase());
        const matchesCategory = $selected.size === 0 || $selected.has(p.category);
        return matchesSearch && matchesCategory;
      })
  );

  // Producto seleccionado
  /** @type {import('svelte/store').Writable<string|null>} */
  const selectedSlug = writable(null);

  onMount(() => {
    const sel = new URLSearchParams($page.url.search).get('select');
    if (sel) selectedSlug.set(sel);
  });

  /** @param {string} cat */
  function toggleCategory(cat) {
    selectedCategories.update(s => {
      const next = new Set(s);
      next.has(cat) ? next.delete(cat) : next.add(cat);
      return next;
    });
  }

  /** @param {string} slug */
  function selectProduct(slug) {
    selectedSlug.update(cur => (cur === slug ? null : slug));
  }
</script>

<Section title="Catálogo de Productos" classId="catalog">
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
        {#each categories as cat}
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
          <img src={prod.image} alt={prod.name} class="card-img-top" />
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
    {/each}

    {#if $filtered.length === 0}
      <div class="col-12">
        <p class="text-center">No se encontraron productos.</p>
      </div>
    {/if}
  </div>
</Section>
