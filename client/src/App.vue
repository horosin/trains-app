<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
    >
      <v-list dense>
        <v-list-tile to="/">
          <v-list-tile-action>
            <v-icon>search</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Wyszukaj połączenie</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile to="/inside">
          <v-list-tile-action>
            <v-icon>directions_railway</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>W trasie</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="primary" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <img src="img/logo.png" style="height:70%;" alt=""> 
      <v-toolbar-title>Podróżuj!</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container>
        <v-layout
          justify-center
        >
          <router-view></router-view>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>

export default {
  name: 'App',
  components: {
  },
  data: () => ({
    drawer: null
  }),
  props: {
    source: String
  },
  mounted: function () {
    // banking.userInfo()
  },
  methods: {

  }
}
</script>

<style>
.app-copy {
  padding-left: 10px;
}
</style>
