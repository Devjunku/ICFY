<template>
  <div class="container">
    <h1>Signup</h1>
    <div class="input-group justify-content-center">
      <div class="mb-3">
          <label for="username" class="form-label">사용자 이름:</label>
          <input type="text" class="form-control" id="username" v-model="credentials.username" placeholder="아이디를 입력하세요">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">비밀번호:</label>
        <input type="password" class="form-control" id="password" v-model="credentials.password" placeholder="비밀번호를 입력하세요">
      </div>
      <div>
        <label for="passwordConfirmation">비밀번호 확인: </label>
        <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" placeholder="비밀번호를 입력하세요">
        <button @click="signup(credentials)">회원가입</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
