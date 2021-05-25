import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"


Vue.use(Vuex)

const MOVIES_LIST_URL = 'http://127.0.0.1:8000/movies/'

export default new Vuex.Store({
  // state를 브라우저에 저장해두기
  // 새로고침해도 정보가 남아있다.
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    review: null,
    username: null,
    userinfo: [],
    search: null,
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
    },
    STORE_USERINFO: function (state, userInfo) {
    state.userinfo = userInfo
    },
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
    },
    storeUserInfo: function ({ commit }, userInfo) {
      commit('STORE_USERINFO', userInfo)
    },
  },
  modules: {
  }
})
