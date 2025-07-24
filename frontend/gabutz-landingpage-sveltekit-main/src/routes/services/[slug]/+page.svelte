<!-- src/routes/services/[slug]/+page.svelte -->
<script>
// @ts-nocheck
  import { fade, slide, fly} from 'svelte/transition';
  import Section from '$lib/components/Section.svelte';
  import { page } from '$app/stores';
  import { services } from '$lib/data/services.js';
  import ImageMarquee from '$lib/components/ImageMarquee.svelte';
  

  // Obtenemos el slug y buscamos el servicio
  $: slug = $page.params.slug;
  $: service = services.find((s) => s.slug === slug);
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
  <!-- Contenedor para animación -->
    <div in:fly={{ y: 20, duration: 400, opacity: 0 }}>
      <h2 class="section_title">Descripción del Servicio</h2>
      <div class="service-info-grid">
        <!-- Columna de texto -->
        <div class="service-text">
          <p>{service.description}</p>
        </div>
        <!-- Columna de bullet points, garantizando siempre un array -->
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

  <!-- Nuevo Carrusel de Imágenes -->
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
    <p>Lo siento, no pudimos encontrar el servicio “{slug}”.</p>
  </Section>
{/if}
