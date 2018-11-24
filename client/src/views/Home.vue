<template>
  <v-layout row wrap>
    <v-flex xs12 sm6 offset-sm3 mb-3>
      <v-select
        v-model="departureSelect"
        :items="stations"
        :error-messages="selectErrors"
        label="Stacja początkowa"
        required
        outline
        @change="$v.select.$touch()"
        @blur="$v.select.$touch()"
    ></v-select>
      <v-select
        v-model="destinationSelect"
        :items="stations"
        :error-messages="selectErrors"
        label="Stacja końcowa"
        required
        outline
        @change="$v.select.$touch()"
        @blur="$v.select.$touch()"
    ></v-select>
    <v-date-picker v-model="picker" :landscape="landscape" :reactive="reactive"></v-date-picker>
    </v-flex>
    <v-flex xs12 sm6 offset-sm3 mb-3>
      <v-btn block color="secondary" to="/inside">Mam bilet</v-btn>
    </v-flex>
    <v-flex xs12 sm6 offset-sm3 mb-3>
      <v-btn block color="secondary" to="/login">Zaloguj się</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>

  export default {
    components: {
    },
    data: () => ({
      stations: ['Kraków Główny','Opoczno Południe','Łódź Kaliska','Warszawa Centralna'],
      departureSelect: '',
      destinationSelect: '',
      selectErrors: []
    }),
    computed: {
      destinationStations: function () {
        return this.stations.filter(station => station !== this.departureSelect)
      }
    }
  }
</script>

<style>
  .basic-input { border-radius: 2px; }
  .layout {
    padding-bottom: 30px;
  }
</style>
