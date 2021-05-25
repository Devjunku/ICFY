<template>
  <div v-if="movie">
    <br>
    <p class="fw-bold">{{ movie.title }}</p>
    <figure class="figure me-4">
      <img class="rounded" :src="moviePosterPath" alt="poster">
      <div class="justify-content-center">
        <div class="container col-6">
          <br>
          <div>
            <p style="text-align:justify; box-sizing: border-box;">{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    </figure>
    <div class="text-warning">
      평점: {{ movie.vote_average }}
    </div>
    <i :class="heartClass" @click="toggleHeart"></i>
    <div class="m-4">
      <button class="btn btn-warning" @click="goToReview">리뷰보기</button>
    </div>
    <div class="mb-3">
      <a :href="'https://www.justwatch.com/kr/검색?q='+movie.title" target="_blank">
        <button class="btn btn-light">어디서 볼 수 있나요?</button>
      </a>
    </div>
    <div>
      <a :href="'https://www.youtube.com/results?search_query='+movie.title" target="_blank">
        <button class="btn btn-danger">관련된 유튜브 동영상 보기</button>
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: null,
      moviePosterPath: null,
      heartClass: "far fa-2x fa-heart heart",
    }
  },
  methods: {
     setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    showMovieDetail: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/' + this.$route.params.movieId,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        this.movie = res.data
        this.moviePosterPath = `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      })
      .catch(err => {
        console.log(err)
        // 도움말에 적기
        this.$router.push({name: 'Login'})
      })
    },
    goToReview: function () {
      this.$router.push({name: 'ReviewPage', params: { movieId: this.movie.id}})
    },
    toggleHeart:  function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/like/' + this.$route.params.movieId +'/',
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        if ( res.data.flag === 1) {
          this.heartClass = "fas fa-2x fa-heart heart"
        } else {
          this.heartClass = "far fa-2x fa-heart heart"
        }
      })
      .catch(err => {
        console.log(err)
      })
    },



  },
  created: function () {
    this.showMovieDetail()
  },
}
</script>

<style scoped>
.heart {
  color: crimson;
}
</style>
