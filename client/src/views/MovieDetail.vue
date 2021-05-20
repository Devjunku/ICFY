<template>
  <div v-if="movie" class="container">
    <p>{{ movie.title }}</p>
    <hr>
    <img :src="moviePosterPath" alt="poster">
    <hr>
    <p>{{ movie.overview }}</p>
    <button @click="goToReview">리뷰보기</button>

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
    }
  },
  methods: {
    showMovieDetail: function () {
      axios({
        url: 'http://127.0.0.1:8000/movies/' + this.$route.params.movieId,
        method: 'get',
      })
      .then(res => {
        console.log(res)
        this.movie = res.data
        this.moviePosterPath = `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      })
    },
    goToReview: function () {
      this.$router.push({name: 'ReviewPage', params: { movieId: this.movie.id}})
    }
  },
  created: function () {
    this.showMovieDetail()
  },
}
</script>

<style>

</style>