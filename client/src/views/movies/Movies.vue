<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MoviesList
         v-for="(movie, idx) in movies" 
        :key="idx"
        :movie="movie"
      />  
    </div>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList'

export default {
  name: 'Movies',
  components: {
    MoviesList
  },
  computed: {
    movies: function () {
      return this.$store.state.movies
    }
  },
  mounted() {
    this.$store.dispatch('createMovies')
  }
}
</script>
