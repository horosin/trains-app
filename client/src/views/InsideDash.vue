<template>
  <v-layout row wrap>
    <v-flex xs12>
      <v-subheader>Godzina przyjazdu</v-subheader>
      <v-card>
        <v-img
          class="white--text"
          height="150px"
          src="img/warszawa.jpg"
        >
          <v-container fill-height fluid>
            <v-layout fill-height>
              <v-flex xs12 align-end flexbox>
                <span class="headline">
                  <div style="width:100%;" class="display-3">18:05</div>
                  <span>Warszawa Centralna</span>
                </span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
        <!-- <v-card-title primary-title>
          <div style="width: 100%">
            <span class="display-3">18:05</span>
          </div>
        </v-card-title> -->
        <v-card-actions>
          <div><strong>5:00</strong> minut opóźnienia.</div>
          <v-spacer></v-spacer>
          <v-btn icon @click="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_up' : 'keyboard_arrow_down' }}</v-icon>
          </v-btn>
        </v-card-actions>
        <v-slide-y-transition>
          <v-card-text v-show="show">
            <timeline :stops="stops"></timeline>
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
    </v-flex>
    <wars v-if="current === 'wars'"></wars>
    <trasa v-if="current === 'trasa'"></trasa>
    <v-flex v-if="current === 'trasa'">
      <v-subheader>Zobacz tez</v-subheader>
      <v-btn color="accent" block @click="go('wars')">Zobacz ofertę WARS! >></v-btn>
    </v-flex>
    <media v-if="current === 'media'"></media>
    <pomoc v-if="current === 'pomoc'"></pomoc>
    <bottom-nav :bottomNav="current" v-on:bottom-menu-change="menuChanged"></bottom-nav>
  </v-layout>
</template>

<script>
import BottomNav from '../components/in-travel/bottom-nav.vue'

import wars from '../components/in-travel/wars.vue'
import trasa from '../components/in-travel/trasa.vue'
import pomoc from '../components/in-travel/pomoc.vue'
import timeline from '../components/in-travel/timeline.vue'
import media from '../components/in-travel/media.vue'

export default {
  data: () => ({
    show: false,
    valid: false,
    password: '',
    email: '',
    ticket: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid'
    ],
    current: "trasa",
    stops: [
      {
        name: 'Kraków',
        time: '16:00'
      },
      {
        name: 'Włoszczowa',
        time: '17:15'
      },
      {
        name: 'Warszawa',
        time: '18:05'
      }
    ]
  }),
  components: {
    BottomNav,
    wars,
    trasa,
    pomoc,
    timeline,
    media
  },
  methods: {
    menuChanged (current) {
      this.current = current
    },
    go (target) {
      this.current = target
    }
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
