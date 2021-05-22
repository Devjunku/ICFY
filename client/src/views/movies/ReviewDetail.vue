<template>
  <div v-if="review" class="container">
    <div class="d-flex">
      <p>{{ review.title }}</p>
    </div>
    
    <hr>
    <p>{{ review.content }}</p>
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
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.review = res.data
      })
    },
  },
  created: function () {
    this.showReviewDetail()
  },
}
</script>

<style>

</style>