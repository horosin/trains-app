<template>
  <v-timeline
    align-top
    dense
  >
    <v-timeline-item
      color="accent lighten-1"
      small
    >
      <v-layout pt-3>
        <v-flex xs3>
          <strong>16:00</strong>
        </v-flex>
        <v-flex>
          <strong>Kraków główny</strong>
        </v-flex>
      </v-layout>
    </v-timeline-item>

    <v-timeline-item
      color="primary lighten-2"
      small
    >
      <v-layout wrap pt-3>
        <v-flex xs3>
          <strong>17:00</strong>
        </v-flex>
        <v-flex>
          <strong>Włoszczowa</strong>
        </v-flex>
      </v-layout>
    </v-timeline-item>

    <v-timeline-item
      color="primary lighten-2"
      small
    >
      <v-layout pt-3>
        <v-flex xs3>
          <strong>18:05</strong>
        </v-flex>
        <v-flex>
          <strong>Warszawa Wschodnia</strong>
        </v-flex>
      </v-layout>
    </v-timeline-item>
  </v-timeline>
</template>
