import Vue from 'vue'
import Router from 'vue-router'
import store from '../store/store'

import Dashboard from '@/components/Dashboard'
import LoginPage from '@/components/LoginPage'
import MainPage from '@/components/MainPage'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/',
      name: 'index',
      component: MainPage
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage,
      meta: { noLogin: true }
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.noLogin || store.state.isUserLoggedIn === true)) {
    next()
  } else {
    next('/login')
  }
})

export default router
