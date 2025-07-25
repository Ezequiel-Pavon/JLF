<!-- src/lib/components/MarqueeExample.svelte -->
<script>
// @ts-nocheck

  import ReviewCard from './ReviewCard.svelte';

  // Tus testimonios
  const reviews = [
    { name: 'Juan Pérez', text: 'Trabajar aquí cambió mi vida.' },
    { name: 'María López', text: 'Excelente ambiente y aprendizaje.' },
    { name: 'Carlos Díaz', text: 'Un equipo muy comprometido.' },
    { name: 'Lucía Gómez', text: 'Crezco día a día gracias al apoyo.' },
    { name: 'Martín Ruiz', text: '¡Altamente recomendable!' }
  ];
</script>

<div class="marquee-wrapper">
  <div class="marquee-track">
    {#each [...reviews, ...reviews] as review, i (i)}
      <ReviewCard {review} />
    {/each}
  </div>
</div>

<style>
.marquee-wrapper {
  overflow: hidden;
  position: relative;
  padding: 2rem 0;
}
.marquee-wrapper:hover .marquee-track {
  animation-play-state: paused;   /* Pausa al hover */
}

.marquee-track {
  display: flex;
  flex-wrap: nowrap;              /* Sin saltos de línea */
  gap: 1rem;
  animation: marquee 20s linear infinite;
}

@keyframes marquee {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-50%);  /* Cubre la mitad del contenido duplicado */
  }
}
</style>
