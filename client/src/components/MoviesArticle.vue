<template>
  <div>
    <hr>
    <div class="parent" @click="showMovieDetail">
      <img :src="moviePosterPath" height="200px" alt="movie">
      <div>
        <h2>{{ movie.title }}</h2>
        <h5>{{ movie.overview }}</h5>
      </div>
    </div>
    <p>{{ movie.vote_average }}</p>  
    <!-- 하트 클릭하려면 따로 빼야 한다. -->
    <i :class="heartClass" @click="toggleHeart"></i>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MoviesArticle',
  data: function () {
    return {
      heartClass: "far fa-2x fa-heart heart",
    }
  },
  props: {
    movie: {
      type: Object
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
      this.$router.push({name: 'MovieDetail', params: { movieId: this.movie.id}, query: { t: new Date().getTime()}})
    },
    toggleHeart:  function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/like/' + this.movie.id +'/',
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
    // 하트가 체크되었는지 확인하기
    checkHeart: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/checkheart/' + this.movie.id +'/',
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        // 좋아요가 있다면
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
  computed: {
    moviePosterPath: function () {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    },
    signal: function () {
      return this.movie.poster_path
    }
  },

  watch: {
    signal: function () {
      this.checkHeart()
    }
  },

  created() {
    this.checkHeart()
  },

  

}
</script>

<style scoped>
.heart {
  color: crimson;
}

.parent {
  display: flex;
}

img:hover {
  border: 2px solid #00e054;
}

h2:hover {
  color: skyblue;
}

h5:hover {
  color: skyblue;
}
</style>