<template>
  <div>
    <br>
    <br>
    <h1>{{ userinfo.username }}의 프로필</h1>
    <button class="btn btn-warning me-3">비밀번호 변경</button>
    <button class="btn btn-danger">회원 탈퇴</button>
    <h3>작성한 리뷰</h3>
     <ProfileReview
         v-for="(review, idx) in reviews" 
        :key="idx"
        :review="review"
      />  
    <h3>작성한 댓글</h3>
    <ProfileComment
         v-for="(comment, idx) in comments" 
        :key="idx"
        :comment="comment"
      />  
  </div>
</template>

<script>
import axios from 'axios'

import ProfileReview from '@/components/ProfileReview'
import ProfileComment from '@/components/ProfileComment'


export default {
  name: 'MyProfile',
   components: {
    ProfileReview,
    ProfileComment
  },
  data: function() {
    return {
    reviews: [],
    comments: [],
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
    }
  },
  computed:  {
    userinfo: function () {
      return this.$store.state.userinfo
    }
  },
  created: function () {
    this.searchInfo()
  },
}
</script>

<style>

</style>