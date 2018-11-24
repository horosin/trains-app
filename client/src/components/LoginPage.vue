<template>
  <v-container align-center justify-center fill-height>
    <v-layout row wrap class="login elevation-4">
      <v-flex xs12 sm10 offset-sm1 mt-2 v-if="errors && errors.length" v-for="(error, index) of errors" :key="index">
        <v-alert :value="true" type="error">{{error.message}}</v-alert>
      </v-flex>
      <v-flex xs12 class="text-xs-center" mt-5>
        <h1>Log In</h1>
      </v-flex>
      <v-flex xs12 sm8 offset-sm2 mt-3>
        <form @submit="onSubmit">
          <v-layout column>
            <v-flex>
              <v-text-field
                name="email"
                label="Email"
                id="email"
                type="email"
                v-model.trim="login.email"
                autocomplete="username email"
                required></v-text-field>
            </v-flex>
            <v-flex>
              <v-text-field
                name="password"
                label="Password"
                id="password"
                type="password"
                v-model.trim="login.password"
                autocomplete="current-password"
                required></v-text-field>
            </v-flex>
            <v-flex class="text-xs-center" mt-5 mb-5>
              <v-btn color="primary" type="submit">Sign In</v-btn>
            </v-flex>
          </v-layout>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import AuthService from '@/services/AuthService'

export default {
  name: 'Login',
  data () {
    return {
      login: {},
      errors: []
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()

      AuthService.login(this.login).then(response => {
        this.$store.dispatch('setToken', response.data.token)
        this.$store.dispatch('setUser', response.data.user)

        this.$router.push({
          name: 'index'
        })
      }).catch(e => {
        this.errors = []
        let error = e;
        if (e.response.status === 400) {
          error = { message: 'Invalid credetials' }
        }
        this.errors.push(error)
      })
    }
  }
}
</script>

<style>
  .login {
    max-width: 500px;
  }
</style>
