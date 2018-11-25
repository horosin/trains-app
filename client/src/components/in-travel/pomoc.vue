<template>
  <v-flex xs12>
    <v-subheader>Masz jakieś pytania lub uwagi?</v-subheader>
				<v-expansion-panel>
					<v-expansion-panel-content
						v-for="(item,i) in items"
						:key="i"
					>
						<div slot="header">{{item.title}}</div>
						<v-card>
              <v-card-text v-if="item.map">
                Wolne miejsca: 
                <div style="width: 100%; overflow-x: scroll;"><img src="https://www.intercity.pl/pl/obrazy/lp/dart/schemat/Dart_pociag_01a.png" alt=""></div>
                <v-toolbar color="transparent" class="elevation-0">
                  <v-icon>keyboard_arrow_left</v-icon>
                  <v-spacer></v-spacer>
                  <v-icon>keyboard_arrow_right</v-icon>
                </v-toolbar>
                <v-divider></v-divider>
                Wagon 1, miejsce 42
                <v-divider></v-divider>
                Wagon 1, miejsce 73
                <v-divider></v-divider>
                Wagon 1, miejsce 76
                <v-divider></v-divider>
              </v-card-text>
							<v-card-text>
                {{item.content}}
                <v-btn v-if="item.button" block color="accent">{{item.button}}</v-btn>  
              </v-card-text>
						</v-card>
					</v-expansion-panel-content>
				</v-expansion-panel>

  </v-flex>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        title: 'Nie odpowiada mi przydzielone miejsce',
        button: 'Zmień miejsce',
        map: true
      },
      {
        title: 'Gdzie jest wagon WARS?',
        button: 'Zobacz plan pociągu'
      },
      {
        title: 'Opóźnienie pociagu powoduje komplikacje w dalszej podróży.',
        button: 'Kontakt z konduktorem'
      },
    ]
  })
}
</script>

