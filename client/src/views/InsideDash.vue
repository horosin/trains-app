<template>
  <v-layout row wrap>
    <v-flex xs12>
      <v-subheader>Informacje o trasie</v-subheader>
      <v-card>
        <v-card-text>
          [basic info]
        </v-card-text>
      </v-card>
    </v-flex>
    <v-flex xs12>
      <v-subheader>Zamów z WARS!</v-subheader>
      <v-card>
        <v-card-text>
          [moah]
        </v-card-text>
      </v-card>
    </v-flex>
    <bottom-nav></bottom-nav>
  </v-layout>
</template>

<script>
import BottomNav from '../components/bottom-nav.vue'


export default {
  data: () => ({
    valid: false,
    password: '',
    email: '',
    ticket: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid'
    ]
  }),
  components: {
    BottomNav
  }
}
</script>

<style>
.login {
  height: 100%;
  width: 100%;
}

/* .creds {
} */

.creds, .ticket {
  height: 50%;
  margin-bottom: 15px;
}
</style>
