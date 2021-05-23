<template>
  <div>
    <br>
    <h1>Login</h1>
    <div class="input-group justify-content-center">
      <div class="mb-3">   
        <input class="form-control" placeholder="아이디를 입력하세요" type="text" id="username" v-model="credentials.username">
      </div>
    </div>
    <div class="input-group justify-content-center">
      <div class="mb-3">   
        <input class="form-control" placeholder="비밀번호를 입력하세요" type="password" id="password" v-model="credentials.password">
      </div>
    </div>
    <div>
      <button class="btn btn-success" @click="login">로그인</button>
    </div>
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
        console.log(res.data)
        this.$store.dispatch('storeUserInfo', res.data)
      })
      .catch(err => {
        console.log(err)
      })

    }  
        
  }
}
</script>