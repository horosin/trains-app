<template>
  <v-layout row wrap>
    <!-- <v-flex xs2 sm1 offset-sm3 mb-3>
      <v-btn><span>o</span></v-btn>
      <div>as</div>
    </v-flex> -->
    <v-flex xs12 sm6 offset-sm3 mb-3>
      <v-select
        v-model="departureSelect"
        :items="stations"
        :error-messages="selectErrors"
        label="Stacja początkowa"
        required
        outline
    ></v-select>
      <v-select
        v-model="destinationSelect"
        :items="stations"
        :error-messages="selectErrors"
        label="Stacja końcowa"
        required
        outline
      ></v-select>
    </v-flex>
      
    <v-flex xs6 sm3 offset-sm3>
      <v-btn block large @click="toggleDatePicker()">{{pickedDate}}</v-btn>
      <v-date-picker
        v-model="pickedDate"
        class="button-align"
        v-if="showDatePicker"
      ></v-date-picker>
      <v-time-picker v-model="pickedTime"
        v-if="showTimePicker"
        class="button-align right-margin"
      ></v-time-picker>
    </v-flex>

    <v-flex xs6 sm3 offset-sm3>
      <v-btn block large @click="toggleTimePicker()">{{pickedTime}}</v-btn>
    </v-flex>

    <v-flex xs12 sm6 offset-sm3 mb-3>
      <v-btn @click="findConnections()" color="accent" block>Wyszukaj połączenie</v-btn>
    </v-flex>

    <v-flex xs12 sm6 offset-sm3 mb-3>
      <v-divider></v-divider>
        <v-btn block color="secondary" to="/inside" class="align-bottom">
          Mam bilet
        </v-btn>
      </v-flex>
  </v-layout>
  
</template>

<script>
  import trains from '../services/trains'
  import router from '../router'

  export default {
    components: {
    },
    data: () => ({
      stations: ['Kraków Główny','Opoczno Południe','Łódź Kaliska','Warszawa Centralna'],
      departureSelect: '',
      destinationSelect: '',
      selectErrors: [],
      pickedDate: '2018-11-25',
      pickedTime: '08:26',
      showDatePicker: false,
      showTimePicker: false
    }),
    computed: {
      destinationStations: function () {
        return this.stations.filter(station => station !== this.departureSelect)
      }
    },
    methods: {
      toggleDatePicker() {
        if (!this.showDatePicker) {
          this.showTimePicker = false;
        }
        this.showDatePicker = !this.showDatePicker;
      },
      toggleTimePicker() {
        // Date().toLocaleTimeString()
        if (!this.showTimePicker) {
          this.showDatePicker = false;
        }
        this.showTimePicker = !this.showTimePicker;
      },
      async findConnections() {
        await trains.setQueryParameters(this.departureSelect, this.destinationSelect, this.pickedTime);
        await router.push('/found-connections');
      }
    }
  }
</script>

<style>
  .basic-input { border-radius: 2px; }
  .container > .layout > .layout.row.wrap {
    padding-bottom: 30px;
  }
  .button-align { position: fixed; z-index: 1 }
</style>
