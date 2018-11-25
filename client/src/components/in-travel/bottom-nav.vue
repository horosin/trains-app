<template>
  <v-bottom-nav
    :active.sync="bottomNav"
    :value="true"
    fixed
    @update:active="changed"
  >
    <v-btn
      color="teal"
      flat
      value="trasa"
    >
      <span>Trasa</span>
      <v-icon>view_agenda</v-icon>
    </v-btn>

    <v-btn
      color="teal"
      flat
      value="wars"
    >
      <span>WARS</span>
      <v-icon>free_breakfast</v-icon>
    </v-btn>

    <v-btn
      color="teal"
      flat
      value="media"
    >
      <span>Filmy</span>
      <v-icon>local_movies</v-icon>
    </v-btn>

    <v-btn
      color="teal"
      flat
      value="pomoc"
    >
      <span>Pomoc</span>
      <v-icon>live_help</v-icon>
    </v-btn>
  </v-bottom-nav>
</template>

<script>
  export default {
    props: ['bottomNav'],
    data () {
      return {
      }
    },
    methods: {
      changed (val) {
        this.$emit('bottom-menu-change', val)
      }
    }
  }
</script>