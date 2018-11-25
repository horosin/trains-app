import axios from 'axios'

export const pkpServer = axios.create({
  baseURL: `http://localhost:5000/trains-app/api/v1.0/`
})

export const banking = axios.create({
  baseURL: 'https://team7.asseco.pl/retail-banking-swagger/api/'
})
