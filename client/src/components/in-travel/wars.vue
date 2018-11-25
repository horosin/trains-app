<template>
  <v-layout row wrap>
    <v-subheader>Nasza oferta</v-subheader>
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
        name: 'Kanapka z szynką',
        img: 'https://www.theblaze.com/wp-content/uploads/2018/01/sandwich.jpg',
        note: 'Klasyka w dobrym wydaniu.',
      },
      {
        name: 'Kajzerka z indykiem',
        img: 'img/food/kanapka.jpg',
        note: 'Wyśmienity wybór na śniadanie!',
      },
      {
        name: 'Smażony Camambert',
        img: 'https://144f2a3a2f948f23fc61-ca525f0a2beaec3e91ca498facd51f15.ssl.cf3.rackcdn.com/uploads/food_portal_data/recipes/recipe/hero_article_image/1554/letterbox_resizeimage593x426xnXdgilhT5j.jpg',
        note: 'Śniadanie dla smakoszy.',
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
