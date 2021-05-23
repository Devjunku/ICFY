<template>
  <div>
    <h4>{{review.title}}</h4>
    <h5>{{review.content}}</h5>
  </div>
</template>

<script>
export default {
  name: 'ProfileReview',
  props: {
    review: {
      type: Object
    }
  },
}
</script>

<style>

</style>