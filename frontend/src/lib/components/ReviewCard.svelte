<script>
  export let review;
</script>

<article class="review-card">
  <div class="avatar">
    <div class="circle"></div>
  </div>
  <h4 class="name">{review.name}</h4>
  <p class="text">“{review.text}”</p>
</article>

<style>
.review-card {
  background: #000000;             /* $primary */
  color: #fffffe;                  /* $white */
  border-radius: 8px;
  padding: 1rem;
  min-width: 200px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  text-align: center;
  flex-shrink: 0;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
}

.review-card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  background: #fd3333;            /* $primary_hover */
}

.review-card .avatar {
  margin: 0 auto 0.5rem;
}
.review-card .circle {
  width: 48px;
  height: 48px;
  background: #fffffe;            /* blanco para destacar */
  border-radius: 50%;
  margin: 0 auto 0.5rem;
}
.review-card .name {
  margin: 0.5rem 0 0.25rem;
  font-size: 1rem;
  font-weight: 600;
}
.review-card .text {
  font-size: 0.9rem;
  color: #fffffe;                 /* texto blanco en el cuerpo */
  margin: 0;
}
</style>
