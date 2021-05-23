<template>
  <div>
    <br>
    <br>
    <h1 v-if="userinfo">{{ userinfo }}</h1>
  </div>
</template>

<script>
export default {
  name: 'MyProfile',
  computed:  {
    userinfo: function () {
      return this.$store.state.userinfo
    }
  },
}
</script>

<style>

</style>