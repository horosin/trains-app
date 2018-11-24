<template>
  <div>
    <v-alert
      v-for="(alert, index) in alerts"
      :key="index"
      :value="true"
      :type="alert.type"
    >
      {{ alert.message }}
    </v-alert>
  </div>
</template>

<script>

export default {
  name: 'Alerts',
  props: [ 'alerts' ],
  data: () => ({
  })
}
</script>
