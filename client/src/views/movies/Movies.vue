<template >
<div class="bg-dark.bg-gradient">
  <br>
  <div class="container">
    <div v-if="posterMode" class="row row-cols-1 row-cols-md-6 g-4">
      <MoviesList
         v-for="(movie, idx) in movies" 
        :key="idx+'a'"
        :movie="movie"
      />  
    </div>
    <div v-else>
      <MoviesArticle
         v-for="(movie, idx) in movies" 
        :key="idx+'b'"
        :movie="movie"
      />  
    </div>
  </div>
</div>
</template>

<script>
import MoviesList from '@/components/MoviesList'
import MoviesArticle from '@/components/MoviesArticle'

export default {
  name: 'Movies',
  components: {
    MoviesList,
    MoviesArticle
  },
  computed: {
    movies: function () {
      return this.$store.state.movies
    },
    posterMode: function () {
      return this.$store.state.posterMode
    },
  },
  mounted() {
    this.$store.dispatch('createMovies')
  }
}
</script>
