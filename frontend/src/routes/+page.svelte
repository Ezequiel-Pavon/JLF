<script lang="ts">
// @ts-nocheck
	import MarqueeExample from '$lib/components/MarqueeExample.svelte';
	import Section from '$lib/components/Section.svelte';
  import { onMount } from 'svelte';
  import { writable, derived, get } from 'svelte/store';
  import { apiFetch } from '$lib/api';
  import { authStore } from '$lib/stores';

	const brands = [
		'/img/img-jlf/Proveedores/chint-logo.png',
		'/img/img-jlf/Proveedores/ducati-energia.png',
		'/img/img-jlf/Proveedores/elibet-logo.png',
		'/img/img-jlf/Proveedores/genrod-logo.jpg',
		'/img/img-jlf/Proveedores/Interlec-logo.svg',
		'/img/img-jlf/Proveedores/kalop-logo.webp',
		'/img/img-jlf/Proveedores/logo_lamy.png',
		'/img/img-jlf/Proveedores/macroled-icon.png',
		'/img/img-jlf/Proveedores/microcontrol-logo.png',
		'/img/img-jlf/Proveedores/neutroluz-logo.png',
		'/img/img-jlf/Proveedores/nian-logo.svg',
		'/img/img-jlf/Proveedores/RBCsitel-logo.png',
		'/img/img-jlf/Proveedores/samet-logo.png',
		'/img/img-jlf/Proveedores/schneider-logo.png',
		'/img/img-jlf/Proveedores/weg-logo.webp',
		];

    interface Service {
      slug: string;
      title: string;
      description?: string;
      images?: string[];
      features?: string[];
    }

    // 1) Traer todos los productos
    const products = writable([]);
    onMount(async () => {
      products.set(await apiFetch('/products/'));
    });

    // 2) Seleccionar los 3 primeros y rellenar con nulls hasta longitud 3
    const featured = derived(products, ($products) => {
      const slice = $products.slice(0, 3);
      while (slice.length < 3) slice.push(null);
      return slice;
    });

    // 3) Cargar servicios
    const servicesList = writable<Service[]>([]);
    onMount(async () => {
      servicesList.set(await apiFetch('/services/'));
    });

    // 4) Tomar los primeros 4, rellenar con null
    const featuredServices = derived(servicesList, ($services) => {
      const slice = $services.slice(0, 4);
      while (slice.length < 4) slice.push(null);
      return slice;
    });

    // 5) Control de formulario de creación
    const showForm = writable(false);
    let newSlug = '';
    let newTitle = '';
    let newDescription = '';
    let newFeatures = '';
    let newFiles: File[] = [];
    let formError = '';

    function handleNewFiles(e) {
      newFiles = Array.from(e.target.files);
    }

    async function submitNewService() {
      formError = '';
      try {
        const fd = new FormData();
        fd.append('slug', newSlug);
        fd.append('title', newTitle);
        fd.append('description', newDescription);
        newFeatures
          .split(',')
          .map(s => s.trim())
          .filter(s => s)
          .forEach(f => fd.append('features', f));
        newFiles.forEach(f => fd.append('images_upload', f, f.name));

        const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/services/`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${get(authStore).accessToken}`
          },
          body: fd
        });
        if (!res.ok) {
          const err = await res.json();
          formError = JSON.stringify(err, null, 2);
          return;
        }
        const created: Service = await res.json();
        servicesList.update(list => [created, ...list]);
        showForm.set(false);
        // reset
        newSlug = newTitle = newDescription = newFeatures = '';
        newFiles = [];
      } catch (e) {
        formError = e.message;
      }
    }

    // 6) Sólo admins ven el botón
    const isAdmin = derived(authStore, $a => !!$a.accessToken);
    const services = derived(authStore, $a => $a.accessToken ? apiFetch('/services/') : []);

    // función para borrar servicios
    async function deleteService(slug: string) {
      if (!confirm(`¿Seguro que querés eliminar el servicio “${slug}”?`)) return;
      try {
        const token = get(authStore).accessToken;
        const res = await fetch(
          `${import.meta.env.VITE_API_BASE_URL.replace(/\/+$/, '')}/services/${slug}/`,
          {
            method: 'DELETE',
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );
        if (!res.ok) {
          // trata de leer detalle
          const err = await res.json().catch(() => ({}));
          throw new Error(err.detail || res.statusText);
        }
        // actualizar store removiendo el eliminado
        servicesList.update(list => list.filter(svc => svc?.slug !== slug));
      } catch (e: any) {
        alert(`Error al borrar: ${e.message}`);
      }
    }
  </script>


 <!--carousel-->
<div id="carouselExampleRide" class="carousel slide" data-bs-ride="true">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="/img/about.jpg" class="d-block w-100" alt="carousel img" width="600" height="350" style="object-fit: cover;">
      <div class="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Some representative placeholder content for the first slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="/img/img-jlf/Carousel/001-QUILMES.jpeg" class="d-block w-100" alt="carousel img" width="600" height="350" style="object-fit: cover;">
      <div class="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Some representative placeholder content for the first slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="/img/img-jlf/Tableros/tablero.jpg" class="d-block w-100" alt="carousel img" width="600" height="350" style="object-fit: cover;">
      <div class="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Some representative placeholder content for the first slide.</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleRide" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleRide" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<!------>

<!-- Start Header -->
<header class="header">
	<div class="container">
		<div class="row align-items-center">
			<div class="col-lg-6 col-md-6 col-12">
				<h1>Soluciones integrales para tus proyectos de electricidad</h1>
				<p>
					Desde hace más de 30 años nos dedicamos a brindarle atención profesional a las empresas e industrias en materia eléctrica, ayudando a que sus procesos productivos se optimicen y no se detengan. 
        </p>
			</div>
			<div class="col-lg-6 col-md-6 col-12">
				<img src="/img/img-jlf/Tableros/tablero.jpg" alt="Hero" class="hero-img img-fluid"/>
			</div>
		</div>
	</div>
</header>
<!-- End Header -->

<!-- Start About -->
<Section
	title="Sobre Nosotros"
	description="Contamos con más de 30 años de experiencia en el rubro, proveemos soluciones integrales en electricidad industrial y domiciliaria con productos de calidad."
	classId="about">
	<div class="row align-items-center">
		<div class="col-lg-5 col-md-6 col-12">
    <img src="/img/tecnico.jpg" alt="Sobre Nosotros" width="420" />
    </div>
		<div class="col-lg-7 col-md-6 col-12">
			<div class="row">
				<div class="col-lg-12 col-md-12 col-12">
					<div class="card">
						<div class="card-body">
							<h3>Soluciones Industriales</h3>
							<p>
								Ofrecemos soluciones eléctricas integrales para la industria, desde automatización hasta distribución eléctrica, cumpliendo con las normativas vigentes y asegurando la máxima seguridad operativa.
							</p>
						</div>
					</div>
				</div>
				<div class="col-lg-12 col-md-12 col-12">
					<div class="card">
						<div class="card-body">
							<h3>Proyectos Domiciliarios</h3>
							<p>
								Desarrollamos proyectos eléctricos domiciliarios personalizados, con atención a los detalles, materiales certificados y un servicio profesional que asegura instalaciones duraderas y seguras
							</p>
						</div>
					</div>
				</div>
				<div class="col-lg-12 col-md-12 col-12">
					<div class="card">
						<div class="card-body">
							<h3>Capacitación</h3>
							<p>
                Brindamos capacitación especializada en instalaciones eléctricas y energías renovables, orientada a profesionales, técnicos y empresas que buscan actualizarse con las últimas normativas y tecnologías del sector.
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</Section>
<!-- End About -->

<!-- START SERVICES Dinámico -->
<Section title="Servicios" classId="service">
  {#if $isAdmin}
    <div class="mb-3 text-end">
      <button class="btn btn-success" on:click={() => showForm.update(v => !v)}>
        {#if $showForm}✖ Cancelar{:else}+ Agregar Servicio{/if}
      </button>
    </div>

    {#if $showForm}
      <div class="card mb-4">
        <div class="card-body">
          {#if formError}
            <div class="alert alert-danger">{formError}</div>
          {/if}
          <div class="row g-3">
            <div class="col-md-4">
              <label for="new-slug" class="form-label">Slug</label>
              <input id="new-slug" class="form-control" bind:value={newSlug} placeholder="p.ej. servicio-nuevo" />
            </div>
            <div class="col-md-4">
              <label for="new-title" class="form-label">Título</label>
              <input id="new-title" class="form-control" bind:value={newTitle} placeholder="Título del servicio" />
            </div>
            <div class="col-md-4">
              <label for="new-features" class="form-label">Features (coma)</label>
              <input id="new-features" class="form-control" bind:value={newFeatures} placeholder="Feat1, Feat2, ..." />
            </div>
            <div class="col-12">
              <label for="new-description" class="form-label">Descripción</label>
              <textarea id="new-description" class="form-control" rows="2" bind:value={newDescription} />
            </div>
            <div class="col-md-6">
              <label for="new-images" class="form-label">Imágenes</label>
              <input id="new-images" type="file" multiple class="form-control" on:change={handleNewFiles} />
            </div>
            <div class="col-12 text-end">
              <button class="btn btn-primary" on:click={submitNewService}>Guardar Servicio</button>
            </div>
          </div>
        </div>
      </div>
    {/if}
  {/if}

  <div class="row">
    {#each $featuredServices as svc}
      {#if svc}
        <div class="col-lg-6 col-md-6 col-12 mb-4 position-relative">
          <!-- Botón de borrar en la esquina superior derecha -->
          {#if $isAdmin}
            <button
              class="btn btn-sm btn-danger position-absolute"
              style="top:0.5rem; right:0.5rem; z-index:10;"
              on:click={() => deleteService(svc.slug)}
            >
              <i class="bi bi-trash"></i>
            </button>
          {/if}

          <a href={`/services/${svc.slug}`} class="card service-card h-100 text-decoration-none">
            {#if svc.images?.length}
              <img src={svc.images[0]} alt={svc.title} class="card-img-top" />
            {:else}
              <div class="placeholder-card card-img-top d-flex align-items-center justify-content-center">
                <i class="bi bi-image placeholder-icon"></i>
              </div>
            {/if}
            <div class="card-body text-center">
              <h3 class="card-title">{svc.title}</h3>
            </div>
          </a>
        </div>
      {:else}
        <!-- Placeholder “Próximamente” -->
        <div class="col-lg-6 col-md-6 col-12 mb-4">
          <div class="card placeholder-card h-100 d-flex align-items-center justify-content-center">
            <div class="placeholder-content text-center">
              <i class="bi bi-hourglass-split fs-1 text-muted"></i>
              <p class="mt-2 text-muted">Próximamente</p>
            </div>
          </div>
        </div>
      {/if}
    {/each}
  </div>
</Section>
<!-- END SERVICES -->


<!-- Start Brands Carousel -->
<Section
  title="NUESTROS PROVEEDORES"
  description="la industria que confía en nosotros"
  classId="brands"
>
	<div class="marquee-wrapper">
		<div class="marquee-track">
			{#each [...brands, ...brands] as src}
			<div class="marquee-item">
				<img src={src} alt="Logo marca" class="img-fluid" />
			</div>
			{/each}
		</div>
	</div>
</Section>
<!-- End Brands Carousel -->

<!-- Start Portfolio -->
<Section
  title="Nuestros Productos"
  description="Algunos de los productos destacados de nuestra empresa"
  classId="portfolio"
>
  <div class="row">
    {#each $featured as prod}
      {#if prod}
        <div class="col-lg-4 col-md-6 col-12 mb-4">
          <div class="card portfolio-card h-100">
            <img
              src={prod.images?.[0] ?? '/img/placeholder.png'}
              alt={prod.name}
              class="card-img-top"
            />
            <div class="card-body text-center">
              <h3 class="card-title">{prod.name}</h3>
              <a href={`/catalog?select=${prod.slug}`} class="btn btn-primary">
                Detalle <i class="bi bi-arrow-right-short"></i>
              </a>
            </div>
          </div>
        </div>
      {:else}
        <!-- Placeholder atractivo -->
        <div class="col-lg-4 col-md-6 col-12 mb-4">
          <div class="card placeholder-card h-100 d-flex align-items-center justify-content-center">
            <div class="placeholder-content">
              <i class="bi bi-box-seam placeholder-icon"></i>
              <p>Próximamente</p>
            </div>
          </div>
        </div>
      {/if}
    {/each}
  </div>
</Section>
<!-- End Portfolio -->

<!-- Start Testimonials -->
<Section
  title="Nuestra Familia"
  description="Historias reales de quienes forman parte del equipo"
  classId="testimonials">
  <MarqueeExample />
</Section>
<!-- End Testimonials -->

<!-- Start Contact -->
<Section
  title="Contáctanos"
  classId="contact"
>
  <div class="row">
    <div class="col-lg-7 col-md-6 col-12">
      <iframe
        src="https://www.google.com/maps?q=Av.+Calchaqu%C3%AD+4230,+B1878+Quilmes+Oeste,+Provincia+de+Buenos+Aires,+Argentina&output=embed"
        allowfullscreen
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="Google Maps - Av. Calchaquí 4230"
        style="width:100%; height:400px; border:0;"
      ></iframe>
    </div>
    <div class="col-lg-5 col-md-6 col-12">
      <div class="card">
        <div class="card-body">
          <div class="content">
            <i class="bi bi-geo-alt"></i>
            <div class="info">
              <h3>Dirección</h3>
              <p>
                Av. Calchaquí 4230, B1878 Quilmes Oeste, Provincia de Buenos Aires, Argentina
              </p>
            </div>
          </div>
          <hr class="hr-dotted" />
          <div class="content">
            <i class="bi bi-envelope"></i>
            <div class="info">
              <h3>Mail</h3>
              <p>info@electrojlf.com.ar</p>
            </div>
          </div>
          <hr class="hr-dotted" />
          <div class="content">
            <i class="bi bi-telephone"></i>
            <div class="info">
              <h3>Teléfono</h3>
              <p>(011) 5353-9408</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</Section>
<!-- End Contact -->

<style lang="scss">
  .placeholder-card {
    background: #f5f5f5;
    border: 2px dashed #ccc;
    color: #666;
    transition: background .3s ease;
    &:hover {
      background: #e9e9e9;
    }
  }
  .placeholder-content {
    text-align: center;
    font-size: 1.1rem;
  }
  .placeholder-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }
</style>
