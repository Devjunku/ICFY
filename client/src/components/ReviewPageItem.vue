<template>
  <div class="text-light">
      <!-- 깔끔하게 하는 방법은 없을까? -->
      <th @click="showReviewDetail" scope="row">{{ review.movie.title }}</th>
      <td @click="showReviewDetail">{{ review.title }}</td>
      <!-- id로만 나온다. -->
      <!-- <td>{{ review.user }}</td> -->
      <td @click="goToProfile">{{ username }}</td>
      <td @click="showReviewDetail">{{ review.created_at }}</td>
      <td v-if="review.created_at !== review.updated_at" @click="showReviewDetail">{{ review.updated_at }}</td>
      <td v-else @click="showReviewDetail">수정되지 않음</td>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'ReviewPageItem',
  data: function () {
    return {
      username: null
    }
  },
  props: {
    review: {
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
    showReviewDetail: function () {
      this.$router.push({name: 'ReviewDetail', params: { reviewId: this.review.id}})
    },
    goToProfile:  function () {
      this.$router.push({name: 'SelectedProfile', params: { userId: this.review.user }})
    }, 
  },
  created: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/find/' + this.review.user + '/',
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        this.username = res.data.username
      })
      .catch(err => {
        console.log(err)
      })
    },
}
</script>

<style>

</style>