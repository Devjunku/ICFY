<template>
  <div class="col">
    <div class="card h-100">
      <img :src="moviePosterPath" class="card-img-top" alt="movie">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <div>{{ movie.overview }}</div>
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
  }
}
</script>

<style>

</style>