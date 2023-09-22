import axios from "axios";

export default defineNuxtPlugin((nuxtApp) => {
  // Criando uma instância do axios com uma baseUrl e um header de autorização
  const api_backend = axios.create({
    baseURL: "https://pokeapi.co/api/v2/pokemon",
    // headers: {
    //   common: {
    //     Authorization: "Basic abcdef123456",
    //   },
    // },
  });

  // Fornecendo a instância do axios para os componentes da aplicação
  nuxtApp.provide("pokeApi", api_backend);
});
