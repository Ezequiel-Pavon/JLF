<script>
	import Section from '$lib/components/Section.svelte';
	import MarqueeExample from '$lib/components/MarqueeExample.svelte';
  import { services } from '../lib/data/services.js';

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
</script>

<!-- Start Header -->
<header class="header">
	<div class="container">
		<div class="row align-items-center">
			<div class="col-lg-6 col-md-6 col-12">
				<h1>Gab<span>utz</span></h1>
				<p>
					Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptatibus non recusandae
					voluptatem ea porro modi?
				</p>
			</div>
			<div class="col-lg-6 col-md-6 col-12">
				<img src="/img/about.jpg" alt="Hero" class="hero-img img-fluid"/>
			</div>
		</div>
	</div>
</header>
<!-- End Header -->

<!-- Start About -->
<Section
	title="About US"
	description="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Soluta, sequi odio esse officia
					repellendus animi ab harum quasi qui at."
	classId="about"
>
	<div class="row align-items-center">
		<div class="col-lg-5 col-md-6 col-12">
			<img src="/img/about.svg" alt="About US" />
		</div>
		<div class="col-lg-7 col-md-6 col-12">
			<div class="row">
				<div class="col-lg-12 col-md-12 col-12">
					<div class="card">
						<div class="card-body">
							<h3>Lorem Ipsum</h3>
							<p>
								Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam accusamus, quas odit,
								asperiores temporibus consequatur eos commodi neque nesciunt dolorem amet doloribus
								cumque velit perspiciatis enim earum corporis veniam! Earum.
							</p>
						</div>
					</div>
				</div>
				<div class="col-lg-12 col-md-12 col-12">
					<div class="card">
						<div class="card-body">
							<h3>Lorem Ipsum</h3>
							<p>
								Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam accusamus, quas odit,
								asperiores temporibus consequatur eos commodi neque nesciunt dolorem amet doloribus
								cumque velit perspiciatis enim earum corporis veniam! Earum.
							</p>
						</div>
					</div>
				</div>
				<div class="col-lg-12 col-md-12 col-12">
					<div class="card">
						<div class="card-body">
							<h3>Lorem Ipsum</h3>
							<p>
								Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam accusamus, quas odit,
								asperiores temporibus consequatur eos commodi neque nesciunt dolorem amet doloribus
								cumque velit perspiciatis enim earum corporis veniam! Earum.
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</Section>
<!-- End About -->

<!-- Start Services -->
<Section title="Servicios" classId="service">
  <div class="row">
    {#each services as service}
      <div class="col-lg-6 col-md-6 col-12 mb-4">
        <div class="card service-card h-100">
          <a href={`/services/${service.slug}`} style="display: block;">
            <img src={service.images[0]} alt={service.title} class="card-img-top" />
          </a>
          <div class="card-body text-center">
            <h3 class="card-title">{service.title}</h3>
          </div>
        </div>
      </div>
    {/each}
  </div>
</Section>
<!-- End Services -->



<!-- Start Brands Carousel -->
<Section
  title="Nuestros Aliados"
  description="Algunas de las marcas que confían en nosotros"
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
    <!-- Producto 1 -->
    <div class="col-lg-4 col-md-6 col-12">
      <div class="card portfolio-card">
        <img
          src="/img/productos/controladores.webp"
          alt="Producto Uno"
          class="card-img-top"
        />
        <div class="card-body text-center">
          <h3 class="card-title">Producto Uno</h3>
          <a href="/productos/producto-uno" class="btn btn-primary">
            Detalle <i class="bi bi-arrow-right-short"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- Producto 2 -->
    <div class="col-lg-4 col-md-6 col-12">
      <div class="card portfolio-card">
        <img
          src="/img/productos/motor.webp"
          alt="Producto Dos"
          class="card-img-top"
        />
        <div class="card-body text-center">
          <h3 class="card-title">Producto Dos</h3>
          <a href="/products/producto-dos" class="btn btn-primary">
            Detalle <i class="bi bi-arrow-right-short"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- Producto 3 -->
    <div class="col-lg-4 col-md-6 col-12">
      <div class="card portfolio-card">
        <img
          src="/img/productos/panelElectrico.webp"
          alt="Producto Tres"
          class="card-img-top"
        />
        <div class="card-body text-center">
          <h3 class="card-title">Producto Tres</h3>
          <a href="/products/producto-tres" class="btn btn-primary">
            Detalle <i class="bi bi-arrow-right-short"></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</Section>
<!-- End Portfolio -->

<!-- Start Testimonials -->
<Section
  title="Lo que dicen nuestros empleados"
  description="Historias reales de quienes forman parte del equipo"
  classId="testimonials"
>
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
