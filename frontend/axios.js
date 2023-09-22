// import axios from "axios";

// export default defineNuxtPlugin((nuxtApp) => {
//   // Criando uma instância do axios com uma baseUrl e um header de autorização
//   const publicApi = axios.create({
//     baseURL: "http://localhost:3000/v1/",
//     headers: {
//       common: {
//         Authorization: "Basic abcdef123456",
//       },
//     },
//   });

//   // Fornecendo a instância do axios para os componentes da aplicação
//   nuxtApp.provide("axios", publicApi);

//   // Injetando a instância do axios nos contextos do Nuxt
//   nuxtApp.inject("axios", publicApi);
// });
