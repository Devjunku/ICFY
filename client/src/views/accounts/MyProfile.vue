<template>
  <div class="container">
    <br>
    <br>
    <div class="d-flex">
      <div>
        <div class="d-flex">
          <h1 class="p-3">{{ userinfo.username }}의 프로필</h1>
          <span class="p-1">
            <p class="p-1">팔로워: {{followers_num}}</p>
            <p class="p-1">팔로잉: {{followings_num}}</p>
          </span>
          <span class="p-1">
            <button @click="clickFollowing">팔로잉 보기</button>
            <button @click="clickFollower">팔로워 보기</button>
          </span>
          <div class="d-inline-block">
            <div v-if="this.showFollowing">
              팔로잉:
              <FollowItem
                v-for="(person, idx) in followings"
                :key="idx+'c'"
                :person="person"
              />
            </div>
            <div v-if="this.showFollower">
              팔로워:
              <FollowItem
                v-for="(person, idx) in followers"
                :key="idx+'d'"
                :person="person"
              />  
            </div>
          </div>
        </div>
        <div class=" justify-content-start">
          <button class="btn btn-warning me-3" @click="toggleForm">비밀번호 변경</button>
          <button class="btn btn-danger me-3" @click="deleteUserCheck">회원 탈퇴</button>
          <aside class="d-inline-block aside-width-height">
            <div>
              <div v-text="messageWarning" class="text-warning mt-3"></div>
              <button v-if="showGuide" class="btn btn-success" @click="guideToggle">도움말 모드 끄기</button>
              <button v-else class="btn btn-success" @click="guideToggle">도움말 모드 켜기</button>
            </div>
            <div v-text="message" class="text-warning mt-3"></div>
            <div v-if="check">
              <input type="password" id="password" v-model="deleteUserPassword" placeholder="비밀번호를 입력하세요">
              <button class="btn btn-danger" @click="deleteUser">확인</button>
            </div>
          </aside>
        </div>
      </div>
      <div>
        
      </div>
    </div>
      <div class="container">
        <section class="d-inline-block section-width-height">
          <div v-if="passwordFlag" class="align-content-baseline">
            <div><input class="form-control mx-auto" type="password" id="password" v-model="password" placeholder="현재 비밀번호를 입력하세요"></div>
            <div><input class="form-control" type="password" id="password" v-model="newPassword" placeholder="새로운 비밀번호를 입력하세요"></div>
            <div><input class="form-control" type="password" id="passwordConfirmation" v-model="newPasswordConfirmation" placeholder="새로운 비밀번호를 재입력하세요"></div>
            <button class="btn btn-warning" @click="passwordChange">확인</button>
          </div>
        </section>
      </div>
    <h3 class="d-flex justify-content-start">좋아요 누른 영화들</h3>
    <div class="container">
      <div class="row row-cols-1 row-cols-md-6 g-4">
        <MoviesList
        v-for="(movie, idx) in likeMovies" 
            :key="idx+'c'"
            :movie="movie"
        />
      </div>
    </div>
    <h3 class="d-flex justify-content-start">작성한 리뷰</h3>
     <ProfileReview
         v-for="(review, idx) in reviews" 
        :key="idx+'a'"
        :review="review"
      />  
    <h3 class="d-flex justify-content-start">작성한 댓글</h3>
    <ProfileComment
         v-for="(comment, idx) in comments" 
        :key="idx+'b'"
        :comment="comment"
      />  
  </div>
</template>

<script>
import axios from 'axios'

import ProfileReview from '@/components/ProfileReview'
import ProfileComment from '@/components/ProfileComment'
import FollowItem from '@/components/FollowItem'
import MoviesList from '@/components/MoviesList'



export default {
  name: 'MyProfile',
   components: {
    ProfileReview,
    ProfileComment,
    FollowItem,
    MoviesList
  },
  data: function() {
    return {
    reviews: [],
    comments: [],
    followings: [],
    followers: [],
    followings_num: null,
    followers_num: null,
    showFollower: false,
    showFollowing: false,
    likeMovies: [],
    passwordFlag: false,
    password: null,
    newPassword: null,
    newPasswordConfirmation: null,
    message: "",
    check: false,
    deleteUserPassword: null,
    messageWarning: null,
    }
  },
  methods: {
    guideToggle: function () {
      this.$store.dispatch('guideToggle')
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    searchInfo: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/profile/${this.userinfo.id}/`,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res.data)
        this.reviews = res.data.review
        this.comments = res.data.comment
      })
      .catch(err => {
        console.log(err)
      })  
    },
    toggleHeart:  function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/like/show/',
        headers: this.setToken(),
      })
      .then(res => {
        this.likeMovies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    clickFollower: function () {
      if (this.showFollower === true){
        this.showFollower = false
      }
      else {
        this.showFollower = true
      }
    },
    clickFollowing: function () {
       if (this.showFollowing === true){
        this.showFollowing = false
      }
      else {
        this.showFollowing = true
      }
    },
    // 팔로우 정보 받아오기 (처음에)
    searchFollow: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/followinfo/${this.userinfo.id}/`,
        headers: this.setToken(),
      })
      .then(res => {
        this.followings = res.data.followings
        this.followers = res.data.followers
        this.followings_num = res.data.followings_num
        this.followers_num = res.data.followers_num
      })
      .catch(err => {
        console.log(err)
      })  
    },
    toggleForm: function () {
      this.passwordFlag = !this.passwordFlag
    },

    passwordChange: function () {
      if (this.newPassword === this.newPasswordConfirmation) {
        axios({
            method: 'put',
            url: 'http://127.0.0.1:8000/accounts/password/',
            data: {
              password: this.password,
              newPassword: this.newPassword,
            },
            headers: this.setToken(),
          })
            .then(res => {
              console.log(res)
              localStorage.setItem('jwt', res.data.token)
              this.password = ""
              this.newPassword = ""
              this.newPasswordConfirmation = ""
              this.message = res.data.message
              if (this.message === 1) {
                // case가 2면 다시 로그인하라는 메시지를 띄우겠다.
                // 자꾸 메인 화면으로 이동해서
                // 이번에는 여기 거쳐서 login으로 가겠다.
                this.$store.dispatch('changeSignal')
                }
                
            })
            .catch(err => {
              console.log(err)
            })
        }
      else {
        this.message = "바꿀 비밀번호 입력과 재입력이 일치하지 않습니다."
      }
    },
    deleteUserCheck: function () {
      this.check = !this.check
    },
    deleteUser: function () {
        axios({
            method: 'delete',
            url: 'http://127.0.0.1:8000/accounts/delete/',
            data: {
              password: this.deleteUserPassword
            },
            headers: this.setToken(),
          })
            .then(res => {
              console.log(res)
              if (res.data.message === 1) {
                this.$store.dispatch('deleteUser')
              }
              else {
                this.messageWarning = res.data.message
              }
            })
            .catch(err => {
              console.log(err)
            })
    }
  },
  computed:  {
    userinfo: function () {
      return this.$store.state.userinfo
    },
    showGuide: function () {
      return this.$store.state.showGuide
    }, 
  },
  created: function () {
    this.searchInfo()
    this.searchFollow()
    this.toggleHeart()
    this.$store.dispatch('myProfileGuide')
  },
}
</script>

<style>

</style>