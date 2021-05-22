<template>
  <div>
    {{ userInfo }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyProfile',
  data: function () {
    return {
      userInfo: null,
    }
  },
  methods: {
    showMyProfile: function () {
      console.log(this.$store.state.username)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.$store.state.username}/`,
        data: this.$store.state.username,
      })
      .then(res => {
        console.log(res)
        this.userInfo = res
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
      this.showMyProfile()  
  },
}
</script>

<style>

</style>