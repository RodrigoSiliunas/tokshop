<template>
  <div class="container py-5">
    <div class="row g-3">
      <div class="col-3 col-lg-4 col-xl-3 d-none d-lg-flex flex-column gap-4">
        <div class="bg-primary rounded-4 pb-5">
          <div class="h-100 bg-white rounded-4 p-2 d-flex flex-column gap-5">
            <div>
              <h5 class="text-primary fw-bolder">PREÇO</h5>
              <label class="form-label">Intervalo de Preço</label>
              <input type="range" class="form-range" />
            </div>
            <div>
              <h5 class="text-primary fw-bolder">GÊNERO</h5>
              <CheckBoxAtom
                :label="genre"
                v-for="(genre, idx) in genres"
                :key="idx"
              />
            </div>
            <div>
              <h5 class="text-primary fw-bolder">CATEGORIA</h5>
              <CheckBoxAtom
                :label="category"
                v-for="(category, idx) in categories"
                :key="idx"
              />
            </div>
          </div>
        </div>
        <ButtonAtom text="FILTRAR" />
      </div>
      <div class="col-12 col-lg">
        <div class="row g-3">
          <div class="col-12 col-md-6 col-xl-4" v-for="product in products" :key="product">
            <ProductCardMolecule />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCardMolecule from "../components/molecules/ProductCardMolecule.vue";
import CheckBoxAtom from "../components/atoms/CheckBoxAtom.vue";
import ButtonAtom from "../components/atoms/ButtonAtom.vue";

export default {
  components: { ProductCardMolecule, CheckBoxAtom, ButtonAtom },
  data() {
    return {
      products: Array.from({ length: 21 }),
      categories: [
        "Malas e Bolsas",
        "Portatéis e Acessórios",
        "Esportes e Fitness",
        "Acessórios para Veículos",
        "Bebê",
        "Laboral e Escolar",
      ],
      genres: ["Masculino", "Feminino"],
    };
  },
};
</script>
