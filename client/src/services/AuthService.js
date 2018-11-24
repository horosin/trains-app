// import Api from '@/services/Api'

export default {
  login (credentials) {
    // return Api().post('auth/login', credentials)
    return Promise.resolve({
      data: {
        token: 'lala',
        user: 'lala'
      }
    })
  }
}
