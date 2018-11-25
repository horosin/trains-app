<template>
  <v-layout row wrap>
    <v-subheader>Polecane filmy</v-subheader>
    <v-flex xs12 v-for="(item,i) in items" :key="i">
      <v-card>
        <v-img
          class="white--text"
          height="150px"
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
          <v-btn flat color="orange">Obejrzyj</v-btn>
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
        name: 'Ekspres polarny ',
        img: 'https://www.portsmouthnh.com/wp-content/uploads/2015/12/the-polar-express-820x445.jpg',
        note: 'Przygodowy',
      },
      {
        name: 'Dziewczyna z pociągu ',
        img: 'https://cdn.natemat.pl/ec3e7ad20c54677806d20830d617c5e3,780,0,0,0.jpg',
        note: 'Sensacyjny',
      },
      {
        name: 'Pociąg do Darjeeling',
        img: 'https://d13ezvd6yrslxm.cloudfront.net/wp/wp-content/images/the-darjeeling-limited-5-700x291.jpg',
        note: 'Komedia, Dramat',
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
