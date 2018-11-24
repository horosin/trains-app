<template>
  <div id="app">
    <v-app id="inspire">
      <v-toolbar dark color="primary">
        <v-toolbar-title><router-link style="color:white; text-decoration:none;" :to="{name: 'index'}">PKP</router-link></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn v-if="$store.state.isUserLoggedIn" flat to="/">Main</v-btn>
          <v-btn v-if="!$store.state.isUserLoggedIn" flat to="/login">Log in</v-btn>
          <v-btn
            v-if="$store.state.isUserLoggedIn"
            flat
            dark
            @click="logout">
            Log Out
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-content>
        <v-container>
          <router-view></router-view>
        </v-container>
      </v-content>
      <v-footer></v-footer>
    </v-app>
  </div>
</template>

<script>
import AppMenu from '@/components/AppMenu';

export default {
  name: 'App',
  components: {
    AppMenu
  },
  methods: {
    logout () {
      this.$store.dispatch('setToken', null)
      this.$store.dispatch('setUser', null)
      this.$router.push({
        name: 'LoginPage'
      })
    }
  }
}
</script>

<style>

.container {
  max-width: 1200px;
}

</style>
