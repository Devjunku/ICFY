<template>
   <div>
    <h1>리뷰 쓰기</h1>
    <div>
      <label for="title">리뷰 제목: </label>
      <input v-if="review" type="text" id="title" v-model="review.title">
    </div>
    <div>
      <label for="content">리뷰 내용: </label>
      <input type="text" id="content" v-model="review.content">
    </div>
    <div>
      <input type="number" v-model="review.review_score" min="0" max="10">
    </div>
    <button @click="submit">리뷰 수정</button>
  </div>
</template>


<script>
import axios from "axios"

export default {
  name: "UpdataReview",
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    
    submit: function () {
      if (this.review.title && this.review.content) {

        axios({
          method: 'put',
        url: 'http://127.0.0.1:8000/movies/community/'+ this.$route.params.reviewId +'/',
        data: {
        title: this.review.title,
        content: this.review.content,
        review_score: this.review.review_score
        },
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'ReviewPage', params: { movieId: this.review.movie } })
        })
        .catch(err => {
          console.log(err)
        })
          }
    }


  },
  computed: {
    review: function () {
      return this.$store.state.review
    }
  },
}
</script>
<style>

</style>