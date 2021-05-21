<template>
  <div class="main container">
    <h1 class="d-flex justify-content-center my-5">Community</h1>
    <div class="row">
      <!-- Board -->
      <section class="col-12 col-lg-10 ps-4">
        <div class="d-none d-lg-block">
          <table class="table table-striped">
            <thead>
            <tr class="table-dark">
              <th scope="col">영화 제목</th>
              <th scope="col">글 제목</th>
              <th scope="col">작성자</th>
              <th scope="col">작성 시간</th>
            </tr>
            </thead>
            <tbody>
            <ReviewPageItem
              v-for="(review, idx) in reviews" 
              :key="idx"
              :review="review"
            />  
            </tbody>
          </table>
        </div>
      
        
        <!-- <div class="d-lg-none mt-5 me-3">
          <article>
            <div class="list-group">
              <a href="#" class="list-group-item list-group-item-action" aria-current="true">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">너무 재밌었습니다.</h5>
                  <small>username11</small>
                </div>
                <div class="mt-2">태극기 휘날리며</div>
                <small>12 minutes ago</small>
              </a>
              <a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">볼만합니다.</h5>
                  <small class="text-muted">username13</small>
                </div>
                <div class="mt-2">기생충</div>
                <small>15 minutes ago</small>
              </a>
              <a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">평범합니다.</h5>
                  <small class="text-muted">username16</small>
                </div>
                <div class="mt-2">바람과 함께 사라지다</div>
                <small>30 minutes ago</small>
              </a>
            </div>
          </article>
        </div> -->

      </section>        
    </div>
    <button @click="goWriteReview">리뷰 쓰기</button>
  </div>


</template>

<script>
import axios from 'axios'

import ReviewPageItem from '@/components/ReviewPageItem'


export default {
  name: 'ReviewPage',
  components: {
    ReviewPageItem
  },
  data: function () {
    return {
      reviews: null,
    }
  },
  methods: {
    requestReviews: function () {
      axios({
        url: 'http://127.0.0.1:8000/movies/' + this.$route.params.movieId +'/community/',
        method: 'get',
      })
      .then(res => {
        console.log(res)
        this.reviews = res.data
      })
      .catch(err => {
          console.log(err)
        })
    },
    goWriteReview: function () {
      this.$router.push({name: 'CreateReview', params: { movieId: this.$route.params.movieId }})
    }
  },
  created: function () {
    this.requestReviews()
  },

}
</script>

<style>

</style>