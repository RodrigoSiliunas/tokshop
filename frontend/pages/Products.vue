<template>
  <div class="container mt-5">
    <div class="row">
      <!-- Barra lateral esquerda com seleção de categorias e faixa de preço -->
      <div class="col-lg-3">
        <h3>Filtrar Produtos</h3>
        <div class="mb-4">
          <h5>Categorias</h5>
          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              value="eletronicos"
              id="categoryElectronics"
              v-model="selectedCategories"
            />
            <label class="form-check-label" for="categoryElectronics">
              Eletrônicos
            </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              value="anime"
              id="categoryAnime"
              v-model="selectedCategories"
            />
            <label class="form-check-label" for="categoryAnime">Anime</label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              value="manga"
              id="categoryManga"
              v-model="selectedCategories"
            />
            <label class="form-check-label" for="categoryManga">Manga</label>
          </div>
        </div>
        <h5>Faixa de Preço</h5>
        <input
          type="range"
          class="form-range"
          id="priceRange"
          min="0"
          max="1000"
          v-model="selectedPrice"
        />
        <div class="d-flex justify-content-between">
          <span>R$ 0</span>
          <span>R$ {{ selectedPrice }}</span>
          <span>R$ 1000</span>
        </div>
      </div>

      <!-- Área central com os cards de produtos -->
      <div class="col-lg-9">
        <h2>Produtos</h2>
        <div class="row">
          <!-- Exemplo de card de produto (você pode repetir isso para vários produtos) -->
          <div class="col-lg-4 mb-4">
            <div class="card">
              <img src="https://i.imgur.com/Th49z9S.png" class="card-img-top" alt="Imagem do Produto">
              <div class="card-body">
                <h5 class="card-title">Título do Produto</h5>
                <p class="card-text">Breve descrição do produto.</p>
                <h6 class="card-subtitle mb-2 text-muted">R$ 299,99</h6>
                <a href="#" class="btn btn-primary">Detalhes</a>
              </div>
            </div>
          </div>
          <!-- Fim do exemplo de card de produto -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedCategories: [], // Array para armazenar as categorias selecionadas
      selectedPrice: 0 // Valor inicial da faixa de preço
    };
  }
};
</script>

<style scoped>
/* Adicione estilos personalizados aqui, se necessário */
</style>
