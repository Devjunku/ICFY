<template>
  <div class="col">
    <div class="card h-100" @click="showMovieDetail">
      <img :src="moviePosterPath" class="card-img-top" alt="movie">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'MoviesList',
  props: {
    movie: {
      type: Object
    }
  },
  computed: {
    moviePosterPath: function () {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    }
  },
  methods: {
    showMovieDetail: function () {
      this.$router.push({name: 'MovieDetail', params: { movieId: this.movie.id}})
    }
  }
}
</script>

<style>

</style>