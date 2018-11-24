import Api from '@/services/Api'

const root = 'projects/'

export default {
  getAll () {
    return Api().get(`${root}`)
  },

  create (data) {
    return Api().post(root, data)
  },

  remove (id) {
    return Api().delete(`${root}${id}`)
  },

  get (id) {
    return Api().get(`${root}${id}`)
  },

  insertTasks (id, tasks) {
    console.log(id, tasks)
    return Api().post(`${root}${id}`, tasks)
  }
}
