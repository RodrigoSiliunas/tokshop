<template>
  <!-- Section: Design Block -->
  <section>
    <!-- Jumbotron -->
    <div
      class="px-4 py-5 px-md-5 text-center text-lg-start"
    >
      <div class="container">
        <div class="row gx-lg-5 align-items-center">
          <div class="col-lg-6 mb-5 mb-lg-0 order-lg-2">
            <h1 class="my-5 display-3 fw-bold ls-tight">
              Registre-se para
              <span class="text-primary" style="">criar sua conta</span>
            </h1>
            <p style="color: hsl(217, 10%, 50.8%)">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet,
              itaque accusantium odio, soluta, corrupti aliquam quibusdam
              tempora at cupiditate quis eum maiores libero veritatis? Dicta
              facilis sint aliquid ipsum atque?
            </p>
          </div>

          <div class="col-lg-6 mb-5 mb-lg-0 order-lg-1">
            <div class="card">
              <div class="card-body py-5 px-md-5">
                <form @submit.prevent="register">
                  <!-- Nome e Sobrenome inputs na mesma linha -->
                  <div class="row mb-4">
                    <div class="col">
                      <div class="form-outline">
                        <label class="form-label" for="name">Nome</label>
                        <input
                          type="text"
                          id="name"
                          class="form-control"
                          v-model="formData.name"
                        />
                      </div>
                    </div>
                    <div class="col">
                      <div class="form-outline">
                        <label class="form-label" for="surname">Sobrenome</label>
                        <input
                          type="text"
                          id="surname"
                          class="form-control"
                          v-model="formData.surname"
                        />
                      </div>
                    </div>
                  </div>

                  <!-- Email input -->
                  <div class="form-outline mb-4">
                    <label class="form-label" for="email">Email</label>
                    <input
                      type="email"
                      id="email"
                      class="form-control"
                      v-model="formData.email"
                    />
                  </div>

                  <!-- Password e Confirm Password inputs na mesma linha -->
                  <div class="row mb-4">
                    <div class="col">
                      <div class="form-outline">
                        <label class="form-label" for="password">Senha</label>
                        <input
                          type="password"
                          id="password"
                          class="form-control"
                          v-model="formData.password"
                        />
                      </div>
                    </div>
                    <div class="col">
                      <div class="form-outline">
                        <label class="form-label" for="confirmPassword">Confirme a senha</label>
                        <input
                          type="password"
                          id="confirmPassword"
                          class="form-control"
                          v-model="formData.confirmPassword"
                        />
                      </div>
                    </div>
                  </div>

                   <!-- Checkbox para concordar com os termos -->
                   <div class="form-check mb-4">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      value=""
                      id="agreeTerms"
                    />
                    <label class="form-check-label" for="agreeTerms">
                      Li e concordo com os
                      <a href="#" style="color: #007bff; text-decoration: underline;">termos de segurança</a> e armazenamento da <i>TokShop</i> &copy;.
                    </label>
                  </div>

                  <button
                    type="submit"
                    class="btn btn-primary btn-block mb-4"
                    style="width: 100%"
                  >
                    Registre-se
                  </button>
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
        name: '',
        surname: '',
        email: '',
        password: '',
        confirmPassword: ''
      }
    };
  },
  methods: {
    register() {
      // Aqui você pode implementar a lógica de registro, enviar os dados para a API, etc.
      // Você pode acessar os dados do formulário em this.formData
    }
  }
};
</script>

<style></style>
