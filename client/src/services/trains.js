import { pkpServer } from '@/services/Api'
import { customers } from '@/services/customers'

const customer = customers[0]

export default {
  queryDepartureStation: '',
  queryDestinationStation: '',
  queryTime: '',

  setQueryParameters(depStation, destStations, time) {
    this.queryDepartureStation = depStation;
    this.queryDestinationStation = destStations;
    this.queryTime = time;
  },
  async getTrainsInfo() {
    const url = 'trains'
    console.error(url)
    return await pkpServer.get(
      url,
      {
        headers: {
        }
      }
    )
  },
  async trainsQueryWithCachedData() {
    return this.trainsQuery(this.queryDepartureStation, this.queryDestinationStation, this.queryTime);
  },
  async trainsQuery(departureStation, destinationStation, startTime) {
    const url = `trains_query?start=${departureStation}&stop=${destinationStation}&start_time=${startTime}`
    console.error(url)
    return await pkpServer.get(
      url,
      {
        headers: {
        }
      }
    )
  }
}