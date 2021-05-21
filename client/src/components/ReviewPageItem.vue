<template>
  <div @click="showReviewDetail">
      <th scope="row">{{ review.movie }}</th>
    <tr>
      <td>{{ review.title }}</td>
      <td>{{ review.user }}</td>
      <td>{{ review.updated_at }}</td>
    </tr>
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