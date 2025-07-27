<script>
	import MarqueeExample from '$lib/components/MarqueeExample.svelte';
	import Section from '$lib/components/Section.svelte';

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
      <img src="/img/img-jlf/Carousel/tablero1.jpg" class="d-block w-100" alt="carousel img" width="600" height="350" style="object-fit: cover;">
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
				<img src="/img/servicios/tablero.jpg" alt="Hero" class="hero-img img-fluid"/>
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

<!-- Start Services -->
<Section
  title="Servicios"
  classId="service">
  <div class="row">
    <!-- Card 1: Tableros-->
    <div class="col-lg-6 col-md-6 col-12">
      <a href="/services/web-design" class="card service-card">
        <img src="/img/servicios/tablero.jpg" alt="tableros" class="card-img-top" />
        <div class="card-body text-center">
          <h3 class="card-title">Tableros</h3>
        </div>
      </a>
    </div>

    <!-- Card 2: Obras-->
    <div class="col-lg-6 col-md-6 col-12">
      <a href="/services/digital-marketing" class="card service-card">
        <img src="/img/servicios/obras.jpg" alt="obras" class="card-img-top" />
        <div class="card-body text-center">
          <h3 class="card-title">Obras</h3>
        </div>
      </a>
    </div>

    <!-- Card 3: Automatizacion -->
    <div class="col-lg-6 col-md-6 col-12">
      <a href="/services/web-development" class="card service-card">
        <img src="/img/servicios/automatizacion.jpg" alt="Web Development" class="card-img-top" />
        <div class="card-body text-center">
          <h3 class="card-title">Automatizacion</h3>
        </div>
      </a>
    </div>

    <!-- Card 4: industria -->
    <div class="col-lg-6 col-md-6 col-12">
      <a href="/services/analytics" class="card service-card">
        <img src="/img/servicios/PLANTA-METALMECANICA.jpg" alt="Analytics" class="card-img-top" />
        <div class="card-body text-center">
          <h3 class="card-title">Industria 4.0</h3>
        </div>
      </a>
    </div>
  </div>
</Section>
<!-- End Services -->


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

    <!-- Puedes agregar más productos siguiendo la misma estructura -->
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
