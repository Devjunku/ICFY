<template>
  <div @click="showReviewDetail" class="text-light">
      <th scope="row">{{ review.movie.title }}</th>
      <td>{{ review.title }}</td>
      <td>{{ review.username }}</td>
      <td>{{ review.created_at }}</td>
      <td v-if="review.created_at !== review.updated_at">{{ review.updated_at }}</td>
      <td v-else>수정되지 않음</td>
  </div>
</template>

<script>
export default {
  name: 'ReviewPageItem',
  props: {
    review: {
      type: Object
    }
  },
  methods: {
    showReviewDetail: function () {
      this.$router.push({name: 'ReviewDetail', params: { reviewId: this.review.id}})
    }
  }
}
</script>

<style>

</style>