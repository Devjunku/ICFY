<template>
  <div id="app">
    <nav class="navbar transparent8 navbar-expand fixed-top navbar-dark d-flex justify-content-between">
      <div class="ms-3">
        <router-link :to="{ name: 'Movies'}" class="navbar-brand">
          <img src="./assets/icfy.png" alt="logo image" height="40">
        </router-link>  
      </div>
      <div>
        <div v-if="isLogin" id="guide" v-text="mainGuide"></div>
        <div v-else id="guide" v-text="loginGuide"></div>
      </div>   
      <div>
        <ul v-if="isLogin" class="navbar-nav">
          <li class="nav-item mx-2">
            <router-link :to="{ name: 'MyProfile'}" class="nav-link text-decoration-none fw-bold text-light">내 프로필</router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link @click.native="logout" to="#" class="nav-link text-decoration-none fw-bold text-light">로그아웃</router-link>
          </li>
        </ul>
        <ul v-else class="navbar-nav">
          <li class="nav-item mx-2">
            <router-link :to="{ name: 'Signup'}" class="nav-link text-decoration-none fw-bold text-light">회원가입</router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link :to="{ name: 'Login'}" class="nav-link text-decoration-none fw-bold text-light">로그인</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <br>
    <br>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
    return {
      loginGuide: "반갑습니다! 로그인을 하신다면 맞춤 영화 추천을 받을 수 있고 영화에 대한 리뷰를 볼 수도 있어요!",
      mainGuide: "로맨스 영화를 좋아하는 admin님 이 영화는 어떠신가요? 마음에 드시면 빨간 버튼을 눌러보세요! 파란 버튼을 눌러서 다른 영화를 추천받을 수도 있습니다.",
       isLogin: false,
    } 
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Movies' })
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  background-color: #222425;
}

#nav {
  padding: 30px;

}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #d0d6d4;
}

.navbar {
  /* 어떤 색으로 할지 정해야 한다. */
  background-color: rgb(44, 43, 43);
  box-shadow: 0px 0px;
}

.transparent8 {
  zoom: 1;
 /* ie 5,6,7 bug fix */
  filter: alpha(opacity=100);
  opacity: 0.8; }


#guide {
  padding: 5px;
}
</style>
