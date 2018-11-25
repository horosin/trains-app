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
							<v-card-text>{{item.content}}</v-card-text>
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
        title: 'Gdzie znajdę konduktora?',
        content: 'Odpowiedź'
      },
      {
        title: 'Gdzie jest wagon WARS?',
        content: 'Odpowiedź'
      },
      {
        title: 'Mam uciążliwych współoasażerów.',
        content: 'Odpowiedź'
      }
    ]
  })
}
</script>

