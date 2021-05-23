<template>
  <h5>{{comment.content}}</h5>
</template>

<script>
export default {
  name: 'ProfileComment',
  props: {
    comment: {
      type: Object
    }
  },
}
</script>

<style>

</style>