<template>
  <!-- Section: Design Block -->
  <section>
    <!-- Jumbotron -->
    <div class="px-4 py-5 px-md-5 text-center text-lg-start">
      <div class="container">
        <div class="row gx-lg-5 align-items-center">
          <div class="col-lg-6 mb-5 mb-lg-0">
            <h1 class="my-5 display-3 fw-bold ls-tight">
              A melhor escolha <br />
              <span class="text-primary" style="">para seu negócio</span>
            </h1>
            <p style="color: hsl(217, 10%, 50.8%)">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet,
              itaque accusantium odio, soluta, corrupti aliquam quibusdam
              tempora at cupiditate quis eum maiores libero veritatis? Dicta
              facilis sint aliquid ipsum atque?
            </p>
          </div>

          <div class="col-lg-6 mb-5 mb-lg-0">
            <div class="card">
              <div class="card-body py-5 px-md-5">
                <form v-on:submit.prevent="login">
                  <!-- 2 column grid layout with text inputs for the first and last names -->

                  <!-- Email input -->
                  <div class="form-outline mb-4">
                    <label class="form-label" for="form3Example3">Email</label>
                    <input
                      type="email"
                      id="form3Example3"
                      class="form-control"
                      v-model="formData.email"
                    />
                  </div>

                  <!-- Password input -->
                  <div class="form-outline mb-4">
                    <label class="form-label" for="form3Example4"
                      >Password</label
                    >
                    <input
                      type="password"
                      id="form3Example4"
                      class="form-control"
                      v-model="formData.password"
                    />
                  </div>

                  <!-- Checkbox -->
                  <div class="form-check d-flex justify-content-left mb-4">
                    <input
                      class="form-check-input me-2"
                      type="checkbox"
                      value=""
                      id="form2Example33"
                      checked
                    />
                    <label class="form-check-label" for="form2Example33">
                      Lembrar senha?
                    </label>
                  </div>

                  <button
                    type="submit"
                    class="btn btn-primary btn-block mb-4"
                    style="width: 100%"
                  >
                    Login
                  </button>

                  <!-- Register buttons -->
                  <div class="text-center">
                    <p>
                      Não tem conta? Você pode
                      <b><a href="">criar uma conta</a></b
                      >!<br />ou, conecte-se com:
                    </p>
                    <button
                      type="button"
                      class="btn btn-link btn-floating mx-1"
                    >
                      <i class="bi bi-facebook"></i>
                    </button>

                    <button
                      type="button"
                      class="btn btn-link btn-floating mx-1"
                    >
                      <i class="bi bi-google"></i>
                    </button>

                    <button
                      type="button"
                      class="btn btn-link btn-floating mx-1"
                    >
                      <i class="bi bi-twitter"></i>
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Jumbotron -->
  </section>
  <!-- Section: Design Block -->
</template>

<script>
export default {
  data() {
    return {
      formData: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    async login() {
      console.log("Hello World!");

      const bulbasaur = await $fetch(
        "https://pokeapi.co/api/v2/pokemon/1",
        "get"
      );
      console.log(bulbasaur);

      const oxe = await this.$pokeApi.get("/45");
      console.log(oxe);
    },
  },
};
</script>

<style></style>
