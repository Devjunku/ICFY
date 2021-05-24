<template>
  <span class="me-3">{{ person.username }}</span>
</template>

<script>
export default {
  name: 'FollowItem',
  props: {
    person: {
      type: Object
    }
  },
}
</script>

<style>

</style>