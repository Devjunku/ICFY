import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '../views/Movies.vue'
import MovieDetail  from '../views/MovieDetail.vue'
import ReviewPage from '../views/ReviewPage.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/:movieId/',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/:movieId/community/',
    name: 'ReviewPage',
    component: ReviewPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
