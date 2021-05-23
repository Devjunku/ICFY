<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('storeUsername', this.credentials.username)
          this.$emit('login')
          this.$router.push({ name: 'Movies' })
          this.storeUserInfo()
        })
        .catch(err => {
          console.log(err)
        })
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    storeUserInfo: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.credentials.username}/`,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        this.$store.dispatch('storeUserInfo', res.data)
      })
      .catch(err => {
        console.log(err)
      })

    }  
        
  }
}
</script>
