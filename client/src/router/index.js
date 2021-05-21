import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '../views/movies/Movies.vue'
import MovieDetail  from '../views/movies/MovieDetail.vue'
import ReviewPage from '../views/movies/ReviewPage.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import CreateReview from '../views/movies/CreateReview.vue'

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
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/community/:reviewPk',
    name: 'CreateReview',
    component: CreateReview,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
