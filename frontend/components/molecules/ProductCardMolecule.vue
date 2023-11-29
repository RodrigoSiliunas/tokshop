<template>
  <div class="d-flex flex-column bg-white rounded-4 gap-1 p-2">
    <div class="row g-2">
      <div class="col-3">
        <div
          class="border border-primary border-2 rounded-2 text-center p-1 lh-1 h-100 d-flex flex-column"
          style="font-size: 0.75rem"
        >
          <span class="text-muted">RESTAM</span>
          <span class="text-bold">21</span>
          <span class="text-muted">UNID.</span>
        </div>
      </div>
      <div class="col-3">
        <div class="border border-primary border-4 bg-primary rounded-2 text-center p-1 lh-1 h-100 d-flex flex-column">
          <span class="fw-bolder text-white">19%</span>
          <i class="bi bi-caret-down-fill text-white"></i>
        </div>
      </div>
    </div>
    <div class="w-100 bg-success" style="height: 250px"></div>
    <div class="d-flex flex-column">
      <span class="fs-3">Mochila Executiva</span>
      <span>
        Uma mochila padrão executivo da linha premium com materiais de...
      </span>
      <span class="fs-6 text-decoration-line-through">R$ 259,99</span>
      <span class="fs-4 text-primary fw-bolder">R$ 210,85</span>
    </div>
    <ButtonAtom text="VENDER" icon="bi bi-cart-fill" />
  </div>
</template>

<script>
import ButtonAtom from "../components/atoms/ButtonAtom.vue";

export default {
  components: { ButtonAtom },
};
</script>
