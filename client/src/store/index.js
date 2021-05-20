import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const MOVIES_LIST_URL = 'http://127.0.0.1:8000/movies/'

export default new Vuex.Store({
  state: {
    movies: [],
  },
  mutations: {
    CREATE_MOVIES: function (state, movies) {
      state.movies = movies
    }
  },
  actions: {
    createMovies: function ({commit}) {
      axios.get(MOVIES_LIST_URL)
      .then(res => {
        console.log(res)
        commit('CREATE_MOVIES', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
