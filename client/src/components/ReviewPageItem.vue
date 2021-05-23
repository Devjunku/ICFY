<template>
  <div @click="showReviewDetail" class="text-light">
      {{ review }}
      <th scope="row">{{ review.movie.title }}</th>
      <td>{{ review.title }}</td>
      <td>{{ review.username }}</td>
      <td>{{ review.updated_at }}</td>
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