<template>
  <div class="container">
    <div class="d-flex justify-content-center">
      <div class="p-2">
        <p>제목: {{review.movie}}</p>
        <p>제목: {{review}}</p>

      </div>
      <div class="p-2">
        <p>내용: {{review.content}}</p>  
      </div>
    </div>
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