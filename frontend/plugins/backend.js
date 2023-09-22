import axios from "axios";

export default defineNuxtPlugin((nuxtApp) => {
  const backend = axios.create({
    baseURL: "http://127.0.0.1/api/v1",
    headers: {
      common: {
        Authorization: "Basic ",
      },
    },
  });

  nuxtApp.provide("backend", backend);
});
