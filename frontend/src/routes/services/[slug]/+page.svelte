<!-- src/routes/services/[slug]/+page.svelte -->
<script context="module" lang="ts">
  import { error } from '@sveltejs/kit';
  import type { LoadEvent } from '@sveltejs/kit';

  /** Carga el servicio desde tu backend */
  export async function load({ fetch, params }: LoadEvent) {
    const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/services/${params.slug}/`);
    if (!res.ok) {
      throw error(res.status, 'Servicio no encontrado');
    }
    const service = await res.json();
    return { service };
  }
</script>

<script lang="ts">
  import { fade, fly } from 'svelte/transition';
  import Section from '$lib/components/Section.svelte';
  import ImageMarquee from '$lib/components/ImageMarquee.svelte';

  // `data` viene inyectado por la función load
  export let data: {
    service: {
      slug: string;
      title: string;
      subtitle?: string;
      description?: string;
      images: string[];
      features: string[];
    };
  };
  const { service } = data;
</script>

{#if service}
  <!-- Hero Banner -->
  <div
    class="service-hero"
    in:fade={{ duration: 400 }}
    style="background-image: url('{service.images[0]}')"
  >
    <div class="overlay">
      <h1>{service.title}</h1>
      <p>{service.subtitle || service.description}</p>
    </div>
  </div>

  <!-- Descripción detallada -->
  <Section classId="service-info">
    <div in:fly={{ y: 20, duration: 400, opacity: 0 }}>
      <h2 class="section_title">Descripción del Servicio</h2>
      <div class="service-info-grid">
        <div class="service-text">
          <p>{service.description}</p>
        </div>
        <ul class="service-features">
          {#each service.features as feat}
            <li>
              <i class="bi bi-check-circle-fill feature-icon"></i>
              <span>{feat}</span>
            </li>
          {/each}
        </ul>
      </div>
    </div>
  </Section>

  <!-- Galería -->
  <Section title="Galería del Servicio" classId="service-gallery">
    <ImageMarquee images={service.images} />
  </Section>

  <!-- CTA -->
  <div class="service-cta" in:fade={{ delay: 200, duration: 400 }}>
    <a href="/contact" class="btn btn-primary btn-lg">
      Contratá este servicio
    </a>
  </div>
{:else}
  <Section title="Servicio no encontrado" classId="service-detail">
    <p>Lo siento, no pudimos encontrar el servicio “{data.service.slug}”.</p>
  </Section>
{/if}
