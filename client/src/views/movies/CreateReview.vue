<template>
   <div>
    <h1>리뷰 쓰기</h1>
    <div>
      <label for="title">리뷰 제목: </label>
      <input type="text" id="title" v-model="reviewTitle">
    </div>
    <div>
      <label for="content">리뷰 내용: </label>
      <input type="text" id="content" v-model="reviewContent">
    </div>
    <div>
      <input v-model="reviewScore" type="number" value="0" min="0" max="10">
    </div>
    <button @click="submit">제출</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateReview',
  data: function () {
    return {
      reviewTitle: null,
      reviewContent: null,
      reviewScore: 0,
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
    submit: function () {
      // 빈 값이 아니라면
      if (this.reviewTitle && this.reviewContent) {

        axios({
          method: 'post',
        url: 'http://127.0.0.1:8000/'+ this.$route.params.movieId +'/community/',
        data: {
        title: this.reviewTitle,
        content: this.reviewContent,
        review_score: this.reviewScore
        },
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'ReviewPage' })
        })
        .catch(err => {
          console.log(err)
        })
          }
    }
  }
}
</script>

<style>

</style>