<template>
  <v-timeline
    align-top
    dense
  >
    <v-timeline-item
      :color="i > 0 ? 'primary lighten-1' : 'accent lighten-1'"
      small
      v-for="(item, i) in stops"
      :key="i"
    >
      <v-layout pt-3>
        <v-flex xs3>
          <strong>{{item.time}}</strong>
        </v-flex>
        <v-flex>
          <strong>{{item.name}}</strong>
        </v-flex>
      </v-layout>
    </v-timeline-item>
  </v-timeline>
</template>

<script>
export default {
  props: [
    'stops'
  ]
}
</script>

