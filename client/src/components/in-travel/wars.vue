<template>
  <v-layout row wrap>
    <v-subheader>Nasza oferta</v-subheader>
    <v-flex xs12 v-for="(item,i) in items" :key="i">
      <v-card>
        <v-img
          class="white--text"
          height="200px"
          :src="item.img"
        >
          <v-container fill-height fluid>
            <v-layout fill-height>
              <v-flex xs12 align-end flexbox>
                <span class="headline">{{item.name}}</span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
        <v-card-title>
          <div>
            <span class="grey--text">{{item.note}}</span><br>
          </div>
        </v-card-title>
        <v-card-actions>
          <v-btn flat color="orange">Zamów</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        name: 'Kajzerka z indykiem',
        img: 'img/food/kanapka.jpg',
        note: 'Wyśmienity wybór na śniadanie!',
      },
      {
        name: 'Kajzerka z indykiem',
        img: 'img/food/kanapka.jpg',
        note: 'Wyśmienity wybór na śniadanie!',
      },
      {
        name: 'Kajzerka z indykiem',
        img: 'img/food/kanapka.jpg',
        note: 'Wyśmienity wybór na śniadanie!',
      },
    ]
  })
}
</script>

<style>
.flex.xs12 {
  margin-bottom: 15px;
}
</style>
