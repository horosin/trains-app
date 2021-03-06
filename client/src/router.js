import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Search from './views/Search.vue'
import Inside from './views/Inside.vue'
import InsideDash from './views/InsideDash.vue'
import FoundConnections from './views/FoundConnections.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/inside',
      name: 'inside',
      component: Inside
    },
    {
      path: '/inside/dash',
      name: 'inside-dash',
      component: InsideDash
    },
    {
      path: '/found-connections',
      name: 'found-connections',
      component: FoundConnections
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
