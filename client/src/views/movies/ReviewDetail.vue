<template>
  <div v-if="review" class="container">
    <div class="d-flex">
      <p>{{ review.title }}</p>
    </div>
    
    <hr>
    <p>{{ review.content }}</p>
    <button @click="updateReview">리뷰 수정</button>
    <button @click="deleteReview">리뷰 삭제</button>
    <div>댓글들</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ReviewDetail',
  data: function () {
    return {
      review: null,
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
    }
  },
  created: function () {
    this.showReviewDetail()
  },
}
</script>

<style>

</style>