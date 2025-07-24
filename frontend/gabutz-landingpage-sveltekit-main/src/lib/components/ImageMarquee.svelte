<!-- src/lib/components/ImageMarquee.svelte -->
<script>
// @ts-nocheck
  import { onMount } from 'svelte';
  export let images = [];

  let trackEl;
  let translateEnd = 0;
  const duration = 20; // segundos para un ciclo completo

  onMount(() => {
    // Usamos requestAnimationFrame para asegurar que el DOM está listo
    requestAnimationFrame(() => {
      // scrollWidth es el ancho total del contenido (dos secuencias de imágenes)
      const fullWidth = trackEl.scrollWidth;
      translateEnd = -fullWidth / 2;
    });
  });
</script>

<div class="image-marquee-wrapper">
  <div
    class="image-marquee-track"
    bind:this={trackEl}
    style="
      --translate-end: {translateEnd}px;
      --marquee-duration: {duration}s;
    "
  >
    {#each [...images, ...images] as img, i (i)}
      <div class="image-marquee-item">
        <img src={img} alt="" />
      </div>
    {/each}
  </div>
</div>

<style>
.image-marquee-wrapper {
  overflow: hidden;
  position: relative;
  padding: 2rem 0;
}
.image-marquee-wrapper:hover .image-marquee-track {
  animation-play-state: paused;
}

.image-marquee-track {
  display: flex;
  flex-wrap: nowrap;
  gap: 1rem;
  /* Usa variables en línea para animación */
  animation: marquee var(--marquee-duration) linear infinite;
}

.image-marquee-item {
  flex: 0 0 auto;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.image-marquee-item:hover {
  transform: scale(1.2);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.image-marquee-item img {
  display: block;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
}

/* Animación basada en el ancho medido */
@keyframes marquee {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(var(--translate-end));
  }
}
</style>
