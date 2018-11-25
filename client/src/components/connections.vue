<template>
  <v-layout row wrap>
  <v-icon class="right-arrow-alignment">keyboard_arrow_right</v-icon>
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
              <p class="text-xs-left title">{{connection.name}}</p>
            </v-flex>
          </v-layout>

          <v-layout>
            <v-flex xs5>
              <p class="text-xs-left subheading">{{connection.departureTime}} - {{connection.arrivalTime}}</p>
            </v-flex>

            <v-flex xs1>
                <v-icon color="primary" class="duration-icon">av_timer</v-icon>
            </v-flex>
            <v-flex xs3>
              <p class="subheading">{{connection.tripDuration}}</p>
            </v-flex>
          </v-layout>
        </div>

        <div class="accent-divider"></div>
        <v-card>
          <v-card-text class="subheading">
            <div class="price-alignment">Klasa 1: <strong>{{connection.firstClassPrice}}.00 PLN</strong></div>
            <div class="price-alignment">Klasa 2: <strong>{{connection.secondClassPrice}}.00 PLN</strong></div>
          </v-card-text><br>
          <v-card-actions>
            <v-btn to='/buy-ticket' color="accent" large block>Kup bilet</v-btn>
          </v-card-actions>
          <v-card-text class="body-2">Stacje pośrednie</strong></v-card-text>

          <timeline :stops="connection.stationsWithTimes"></timeline>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-flex>
  </v-layout>

</template>

<script>
  // import connection from './connections/connection'
  import trains from '../services/trains'
  import timeline from './in-travel/timeline'

  export default {
    data: () => ({
      panel: [false, true, false],
      departureStation: 'Kraków Główny',
      destinationStation: 'Warszawa Centralna',
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
          secondClassPrice: '48'
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
          secondClassPrice: '74'        }
      ]
    }),
    mounted: function () {
      trains.trainsQueryWithCachedData().then(response => {
        const serverFormatConnections = response.data.train;
        let clientFormatConnections = serverFormatConnections.map(connection => {
          // let newConnection = Object.assign({}, connection);
          let newConnection = {}
          newConnection.name = connection.name;
          newConnection.tripDuration = connection.duration;
          newConnection.firstStation = connection.start;
          newConnection.lastStation = connection.stop;
          let depTime = new Date(connection.start_time);
          newConnection.departureTime = `${depTime.getHours()}:${depTime.getMinutes()}`;
          let arrTime = new Date(connection.stop_time);
          newConnection.arrivalTime = `${arrTime.getHours()}:${arrTime.getMinutes()}`;

          let stationsWithEnds = connection.stations;
          stationsWithEnds.unshift(connection.start);
          stationsWithEnds.push(connection.stop);
          newConnection.stations = stationsWithEnds;

          const stationsTimes = connection.stations_time.map(time => {
            const newTime = new Date(time);

            const minutes = newTime.getMinutes();
            const stringMinutes = minutes > 9 ? minutes : '0' + minutes;
            return `${newTime.getHours()}:${stringMinutes}`;
          });
          stationsTimes.unshift(newConnection.departureTime);
          stationsTimes.push(newConnection.arrivalTime);

          newConnection.stationsWithTimes = newConnection.stations.map( (station, index) => {
            return { name: station, time: stationsTimes[index]}
          })

          newConnection.firstClassPrice = connection.price1;
          newConnection.secondClassPrice = connection.price2;
          return newConnection;
          
        });
        this.connections = clientFormatConnections || [];
      })
    },
    components: {
      timeline
    },
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

.right-arrow-alignment {
  position: absolute; 
  left: 46%;
  top: 45px
}

.duration-icon {
  position: relative; 
  bottom: 1px;
}

.price-alignment {
  float: left;
  margin-right: 15px;
}

.accent-divider {
  height: 1px;
background-image: radial-gradient(#FF5F19 5%, white 95%);
}
</style>
