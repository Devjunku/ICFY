<template>
  <div class="container">
    <br>
    <h1>Signup</h1>
    <div class="input-group justify-content-center">
      <div class="mb-3">      
          <input type="text" class="form-control" id="username" v-model="credentials.username" placeholder="아이디를 입력하세요">
      </div>
    </div>
      <!-- <button class="btn btn-success mb-3" @click="checkId">아이디 중복 체크하기</button> -->
    <div class="input-group justify-content-center">
      <div class="mb-3">
        <input type="password" class="form-control" id="password" v-model="credentials.password" placeholder="비밀번호를 입력하세요">
      </div>
    </div>
    <div class="input-group justify-content-center">
      <div>
        <input type="password" class="form-control" id="passwordConfirmation" v-model="credentials.passwordConfirmation" placeholder="비밀번호를 재입력하세요">
      </div>
    </div>
    <div v-if="different" class="text-danger mt-3">두 비밀번호가 일치하지 않습니다.</div>
    <div class="mt-3">
      <button class="btn btn-warning" @click="signup">회원가입</button>
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
      },
      different: false
    }
  },
  methods: {
    signup: function () {
      if (this.credentials.password === this.credentials.passwordConfirmation) {
        console.log(1)
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
        this.different = false
      }
      else {
        this.different = true
      }
    },
    // checkId: function () {
    //   axios({
    //     method: 'post',
    //     url: 'http://127.0.0.1:8000/accounts/check/',
    //     data: this.credentials,
    //   })
    //     .then(res => {
    //       console.log(res)
    //       this.$router.push({ name: 'Login' })
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // }
  }
}
</script>
