<template>
  <div class="login">
    <div class="creds">
      <v-form v-model="valid" d-flex>
        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>
        <v-text-field
          v-model="password"
          label="Hasło"
          required
        ></v-text-field>
      </v-form>
    </div>
    <div class="ticket">

    </div>
  </div>
  <!-- <v-flex d-flex>
    <v-layout row wrap>
      <v-flex d-flex xs12>
        <v-card>
          <v-card-text>

          
          </v-card-text>
        </v-card>
      
      </v-flex>
      <v-flex d-flex xs12>
        <v-card>
          <v-card-text>
            <v-form v-model="valid">
              <v-text-field
                v-model="ticket"
                label="Numer biletu"
              ></v-text-field>
            </v-form>
          </v-card-text>
        </v-card>
        
      </v-flex>
    </v-layout>
  </v-flex> -->
</template>

<script>

  export default {
    data: () => ({
      valid: false,
      password: '',
      email: '',
      ticket: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ]
    })
  }
</script>

<style>
.login {
  height: 100%;
  width: 100%;
}

/* .creds {
} */

.creds, .ticket {
  height: 50%;
  background: white;
  margin-bottom: 15px;
}
</style>
