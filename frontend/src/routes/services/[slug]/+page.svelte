<!-- src/routes/services/[slug]/+page.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { apiFetch } from '$lib/api';
  import Section from '$lib/components/Section.svelte';
  import ImageMarquee from '$lib/components/ImageMarquee.svelte';
  import { fade, fly } from 'svelte/transition';

  interface Service {
    slug: string;
    title: string;
    subtitle?: string;
    description: string;
    features?: string[];
    images?: string[];
  }

  let service: Service | null = null;
  let errorMsg = '';
  let isLoading = true;

  onMount(async () => {
    const { slug } = $page.params;
    try {
      const data = await apiFetch(`/services/${slug}/`);
      service = data as Service;
    } catch (e: any) {
      errorMsg = e.detail ?? e.message ?? 'Error desconocido';
    } finally {
      isLoading = false;
    }
  });
</script>

{#if isLoading}
  <Section>
    <p>Cargando servicio…</p>
  </Section>
{:else if errorMsg}
  <Section title="Error" classId="service-detail">
    <p>{errorMsg}</p>
  </Section>
{:else if service}
  <div
    class="service-hero"
    in:fade={{ duration: 400 }}
    style={`background-image: url(${service.images?.[0] ?? '/img/placeholder.png'})`}
  >
    <div class="overlay">
      <h1>{service.title}</h1>
      <p>{service.subtitle ?? service.description}</p>
    </div>
  </div>

  <Section classId="service-info">
    <div in:fly={{ y: 20, duration: 400, opacity: 0 }}>
      <h2 class="section_title">Descripción del Servicio</h2>
      <div class="service-info-grid">
        <div class="service-text">
          <p>{service.description}</p>
        </div>
        <ul class="service-features">
          {#each service.features ?? [] as feat}
            <li>
              <i class="bi bi-check-circle-fill feature-icon"></i>
              <span>{feat}</span>
            </li>
          {/each}
        </ul>
      </div>
    </div>
  </Section>

  <Section title="Galería del Servicio" classId="service-gallery">
    <ImageMarquee images={service.images ?? []} />
  </Section>

  <div class="service-cta" in:fade={{ delay: 200, duration: 400 }}>
    <a href="/contact" class="btn btn-primary btn-lg">
      Contratá este servicio
    </a>
  </div>
{/if}

<style>
  /* Tus estilos */
</style>
