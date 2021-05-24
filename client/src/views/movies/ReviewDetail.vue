<template>
  <div v-if="review" class="container">
    <div class="d-flex">
      <p>{{ review.title }}</p>
    </div>
    <hr>
    <p>{{ review.content }}</p>
    <div v-if="requestUser.id === review.user">
      <button @click="updateReview">리뷰 수정</button>
      <button @click="deleteReview">리뷰 삭제</button>
    </div>
    <div>댓글들</div>
    <CommentItem
      v-for="(comment, idx) in comments" 
      :key="idx"
      :comment="comment"
      @delete-comment="showReviewDetail"
      @update-comment="showReviewDetail"
    />
     <div>
      <label for="content">댓글: </label>
      <input type="text" id="content" v-model="commentContent" @keyup.enter="createComment">
    </div>
    <button @click="createComment">댓글 쓰기</button>
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem'

import axios from 'axios'
export default {
  name: 'ReviewDetail',
  components: {
    CommentItem
  },
  data: function () {
    return {
      review: null,
      comments: [],
      commentContent: null,
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
    showReviewDetail: function () {
      axios({
        url: 'http://127.0.0.1:8000/movies/community/' + this.$route.params.reviewId,
        method: 'get',
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        this.review = res.data
        this.comments = res.data.comment_set
      })
    },
    deleteReview: function () {
      axios({
        url: 'http://127.0.0.1:8000/movies/community/' + this.$route.params.reviewId,
        method: 'delete',
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push( {name: 'ReviewPage', params: {movieId: res.data.movie_id} })
        })
        .catch((err) => {
          console.log(err)
        })
    },

    // 이 리뷰를 중앙 저장소에 저장하겠다.
    updateReview: function () {
      this.$store.dispatch('updateReview', this.review)
      this.$router.push( {name: 'UpdateReview'})
    },
    
    createComment: function () {
      // 빈 값이 아니라면
      if (this.commentContent) {

        axios({
          method: 'post',
        url: 'http://127.0.0.1:8000/movies/community/'+ this.review.id +'/',
        data: {
        content: this.commentContent,
        },
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.showReviewDetail()
          // 빈 칸으로 만들기
          this.commentContent =""
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  },
  computed: {
    requestUser: function () {
      return this.$store.state.userinfo
    }
  },
  created: function () {
    this.showReviewDetail()
  },
}
</script>

<style>

</style>