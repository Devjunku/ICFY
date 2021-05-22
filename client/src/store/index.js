import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const MOVIES_LIST_URL = 'http://127.0.0.1:8000/movies/'

export default new Vuex.Store({
  state: {
    movies: [],
    review: null,
    username: '',
  },
  mutations: {
    CREATE_MOVIES: function (state, movies) {
      state.movies = movies
    },
    UPDATE_REVIEW:function (state, review) {
      state.review = review
    },
    STORE_USERNAME: function (state, username) {
      state.username = username
    }
  },
  actions: {
    createMovies: function ({commit}) {
      axios.get(MOVIES_LIST_URL)
      .then(res => {
        // console.log(res)
        commit('CREATE_MOVIES', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateReview: function ({ commit }, review) {
      commit('UPDATE_REVIEW', review)
    },
    storeUsername: function ({ commit }, username) {
      commit('STORE_USERNAME', username)
    }
  },
  modules: {
  }
})
