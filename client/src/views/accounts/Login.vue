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
          console.log(res)
          console.log(this.credentials.username)
          this.$store.dispatch('storeUsername', this.credentials.username)
          this.$emit('login')
          this.$router.push({ name: 'Movies' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>