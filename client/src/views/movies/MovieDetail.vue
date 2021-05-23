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
    <div class="m-4">
      <button class="btn btn-warning" @click="goToReview">리뷰보기</button>
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
    }
  },
  methods: {
    showMovieDetail: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/' + this.$route.params.movieId,
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