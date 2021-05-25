<template>
  <div>
    <br>
    <br>
    <h1>{{this.username}}의 프로필</h1>
    <div>
      <h4>팔로워 수: {{followers_num}}</h4>
      <h4>팔로잉 수: {{followings_num}}</h4>
      <button class="btn btn-primary" @click="clickBtn">FOLLOW</button>
    </div>
    <div>
      <button @click="clickFollower">팔로워 보기</button>
      <button @click="clickFollowing">팔로잉 보기</button>
    </div>
    <div v-if="this.showFollowing">
      팔로잉:
      <FollowItem
        v-for="(person, idx) in followings"
        :key="idx+'c'"
        :person="person"
      />
    </div>
    <div v-if="this.showFollower">
      팔로워:
      <FollowItem
         v-for="(person, idx) in followers"
        :key="idx+'d'"
        :person="person"
      />  
    </div>

    <h3>좋아요 누른 영화들</h3>
    <div class="container">
      <div class="row row-cols-1 row-cols-md-6 g-4">
        <MoviesList
        v-for="(movie, idx) in likedMovies" 
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
import FollowItem from '@/components/FollowItem'
import MoviesList from '@/components/MoviesList'


export default {
  name: 'SelectedProfile',
  components: {
    ProfileReview,
    ProfileComment,
    FollowItem,
    MoviesList
  },
  data: function() {
    return {
    reviews: [],
    comments: [],
    followings: [],
    followers: [],
    followings_num: null,
    followers_num: null,
    showFollower: false,
    showFollowing: false,
    username: null,
    likedMovies: [],
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
    // 리뷰 댓글 정보 불러오기
    searchInfo: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/profile/${this.$route.params.userId}/`,
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
    // 팔로우 토글
    clickBtn: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/follow/${this.$route.params.userId}/`,
        headers: this.setToken(),
      })
      .then(res => {
        this.followings = res.data.followings
        this.followers = res.data.followers
        this.followings_num = res.data.followings_num
        this.followers_num = res.data.followers_num
      })
      .catch(err => {
        console.log(err)
      })  
    },
    // 팔로우 정보 받아오기 (처음에)
    searchFollow: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/followinfo/${this.$route.params.userId}/`,
        headers: this.setToken(),
      })
      .then(res => {
        this.followings = res.data.followings
        this.followers = res.data.followers
        this.followings_num = res.data.followings_num
        this.followers_num = res.data.followers_num
      })
      .catch(err => {
        console.log(err)
      })  
    },

    // 프로필 유저네임 받아오기
    searchUserName: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/find/${this.$route.params.userId}/`,
        headers: this.setToken(),
      })
      .then(res => {
        this.username = res.data.username
      })
      .catch(err => {
        console.log(err)
      })  
    },

    clickFollower: function () {
      if (this.showFollower === true){
        this.showFollower = false
      }
      else {
        this.showFollower = true
      }
    },
    clickFollowing: function () {
       if (this.showFollowing === true){
        this.showFollowing = false
      }
      else {
        this.showFollowing = true
      }
    },
    toggleHeart:  function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/like/show/${this.$route.params.userId}/`,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res.data)
        this.likedMovies = res.data
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
    this.searchFollow()
    this.searchUserName()
    this.toggleHeart()
  },
}
</script>

<style>

</style>