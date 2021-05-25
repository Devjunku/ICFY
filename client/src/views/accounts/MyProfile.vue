<template>
  <div>
    <br>
    <br>
    <h1>{{ userinfo.username }}의 프로필</h1>
    <button class="btn btn-warning me-3">비밀번호 변경</button>
    <button class="btn btn-danger">회원 탈퇴</button>
    <h3>좋아요 누른 영화들</h3>
    <div class="container">
      <div class="row row-cols-1 row-cols-md-6 g-4">
        <MoviesList
        v-for="(movie, idx) in likeMovies" 
            :key="idx+'c'"
            :movie="movie"
        />
      </div>
    </div>
    <h3>작성한 리뷰</h3>
     <ProfileReview
         v-for="(review, idx) in reviews" 
        :key="idx+'a'"
        :review="review"
      />  
    <h3>작성한 댓글</h3>
    <ProfileComment
         v-for="(comment, idx) in comments" 
        :key="idx+'b'"
        :comment="comment"
      />  
  </div>
</template>

<script>
import axios from 'axios'

import ProfileReview from '@/components/ProfileReview'
import ProfileComment from '@/components/ProfileComment'
import MoviesList from '@/components/MoviesList'


export default {
  name: 'MyProfile',
   components: {
    ProfileReview,
    ProfileComment,
    MoviesList
  },
  data: function() {
    return {
    reviews: [],
    comments: [],
    likeMovies: [],
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
    searchInfo: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/profile/${this.userinfo.id}/`,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res.data)
        this.reviews = res.data.review
        this.comments = res.data.comment
      })
      .catch(err => {
        console.log(err)
      })  
    },
    toggleHeart:  function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/like/show/',
        headers: this.setToken(),
      })
      .then(res => {
        this.likeMovies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },

  },
  computed:  {
    userinfo: function () {
      return this.$store.state.userinfo
    }
  },
  created: function () {
    this.searchInfo()
    this.toggleHeart()
  },
}
</script>

<style>

</style>