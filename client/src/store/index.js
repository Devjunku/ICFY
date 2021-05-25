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
    posterMode: true,
    guide: "로그인을 하면 맞춤 영화 추천을 받을 수 있고 영화에 대한 리뷰를 볼 수도 있어요!"
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
    MODE_TOGGLE: function (state) {
      if (state.posterMode === true) {
        state.posterMode = false
      } else {
        state.posterMode = true
      }
    },
    LOGIN_GUIDE: function (state) {
      state.guide = "도움말 오른쪽의 아이콘을 클릭하면 영화의 레이아웃을 변경할 수 있습니다."
    },
    LOGOUT_GUIDE: function (state) {
      state.guide = "로그인을 하면 맞춤 영화 추천을 받을 수 있고 영화에 대한 리뷰를 볼 수도 있어요!"
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
    },
    storeUserInfo: function ({ commit }, userInfo) {
      commit('STORE_USERINFO', userInfo)
    },
    modeToggle: function ({ commit }) {
      commit('MODE_TOGGLE')
    },
    loginGuide: function ({ commit }) {
      commit('LOGIN_GUIDE')
    },
    logoutGuide: function ({ commit }) {
      commit('LOGOUT_GUIDE')
    },
  },
  modules: {
  }
})
