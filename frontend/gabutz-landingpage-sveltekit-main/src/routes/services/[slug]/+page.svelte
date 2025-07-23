<!-- src/routes/services/[slug]/+page.svelte -->
<script context="module">
  import { error } from '@sveltejs/kit';
  import { services } from '../data.js';

  // @ts-ignore
  export async function load({ params }) {
    const service = services.find((s) => s.slug === params.slug);
    if (!service) {
      throw error(404, 'Servicio no encontrado');
    }
    return { service };
  }
</script>

<script>
  import Section from '$lib/components/Section.svelte';
  // @ts-ignore
  export let data;
  // @ts-ignore
  const { service } = data;
</script>

{#if service}
  <Section title={service.title} description={service.description} classId="service-detail">
    <div class="row">
      {#each service.images as img}
        <div class="col-md-6 col-12 mb-4">
          <img src={img} alt={service.title} class="img-fluid rounded" />
        </div>
      {/each}
    </div>
  </Section>
{:else}
  <p>Lo siento, el servicio solicitado no se encontró.</p>
{/if}
