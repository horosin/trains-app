<template>
  <v-layout row wrap>
  <v-flex xs6 sm6 offset-sm3>
    <p class="text-xs-center display-1">{{departureStation}}</p>
  </v-flex>
  <v-flex xs6 sm6 offset-sm3>
    <p class="text-xs-center display-1">{{destinationStation}}</p>
  </v-flex>
  <v-flex xs12 sm6 offset-sm3>
   <p class="text-xs-center subheading">{{date}}</p>
  </v-flex>


  <v-flex xs12 sm6>
    <v-subheader>Znalezione połączenia</v-subheader>
    <v-expansion-panel
      v-model="panel"
      expand>
      <v-expansion-panel-content
        v-for="(connection,i) in connections"
        :key="i"
      >
        <!-- <connection connection="connection"></connection> -->
        <div slot="header">
          <v-layout>
            <v-flex xs12>
              <p class="text-xs-left title" color="accent">{{connection.name}}</p>
            </v-flex>
          </v-layout>

          <v-layout>
            <v-flex xs12>
              <p class="text-xs-left" color="accent">{{connection.departureTime}} - {{connection.arrivalTime}}</p>
            </v-flex>
          </v-layout>

          <v-layout>
            <v-flex xs1>
                <v-icon color="accent">av_timer</v-icon>
            </v-flex>
            <v-flex xs3>
              <p 
              color="accent">{{connection.tripDuration}}</p>
            </v-flex>
          </v-layout>
        </div>

        <v-card>
          <v-card-text class="subheading">Klasa 1: <strong>{{connection.firstClassPrice}}.00 PLN</strong></v-card-text>
          <v-card-text class="subheading">Klasa 2: <strong>{{connection.secondClassPrice}}.00 PLN</strong></v-card-text>
          <timeline></timeline>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-flex>
  </v-layout>

</template>

<script>
  // import connection from './connections/connection'
  import timeline from './in-travel/timeline'

  export default {
    data: () => ({
      panel: [false, true, false],
      departureStation: 'Kraków Główny',
      destinationStation: 'Opoczno Południe',
      date: '25 sierpnia 2018',
      connections: [
        {
          name: 'IC 5322 Kolberg',
          firstStation: 'Kraków Główny',
          lastStation: 'Opoczno Południe',
          stations: ['Kraków Główny', 'Miechów', 'Opoczno Południe'],
          departureTime: '9:04',
          arrivalTime: '12:42',
          date: '25/11',
          tripDuration: '3:38',
          firstClassPrice: '63',
          secondClassPrice: '48',
          time: 'asd'
        },
        { 
          name: 'TLK 13101 Malinowski',
          firstStation: 'Kraków Główny',
          lastStation: 'Opoczno Południe',
          stations: ['Kraków Główny', 'Miechów', 'Opoczno Południe'],
          departureTime: '11:56',
          arrivalTime: '14:02',
          date: '25/11',
          tripDuration: '2:06',
          firstClassPrice: '98',
          secondClassPrice: '74',
          time: 'asdf'
        },
        {
          name: 'Lokata mobilna',
          time: '15:11'
        },
        {
          name: 'Lokata urodzinowa',
          time: '16:10'
        }
      ]
    }),
    components: {
      timeline
    }
  }

</script>

<style>
v-card-title {
  font-size: 3em;
}

.deposit-pct {
  font-size: 20px;
  line-height: 36px;
}

.deposit-text {
  line-height: 36px;
}
</style>
