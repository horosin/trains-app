<template>
  <v-bottom-nav
    :active.sync="bottomNav"
    :value="true"
    absolute
    color="transparent"
  >
    <v-btn
      color="teal"
      flat
      value="recent"
    >
      <span>Trasa</span>
      <v-icon>view_agenda</v-icon>
    </v-btn>

    <v-btn
      color="teal"
      flat
      value="favorites"
    >
      <span>WARS</span>
      <v-icon>free_breakfast</v-icon>
    </v-btn>

    <v-btn
      color="teal"
      flat
      value="nearby"
    >
      <span>Pomoc</span>
      <v-icon>live_help</v-icon>
    </v-btn>
  </v-bottom-nav>
</template>

<script>
  export default {
    data () {
      return {
        bottomNav: 'recent'
      }
    }
  }
</script>