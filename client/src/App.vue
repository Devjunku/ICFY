<template>
  <div id="app">
    <nav class="navbar navbar-expand fixed-top navbar-dark bg-dark d-flex justify-content-between">
      <div class="ms-3">
        <router-link :to="{ name: 'Movies'}" class="navbar-brand">
          <img src="./assets/logo.png" alt="logo image" height="35">
        </router-link>  
      </div>
      <div>
        <input type="text" size=35 class="ms-3" v-model="searchKeyword" @keyup.enter="searchEnter" placeholder="영화 제목을 검색하세요">
      </div>
      <div>
        <ul v-if="isLogin" class="navbar-nav">
          <li class="nav-item mx-2">
            <router-link :to="{ name: 'MyProfile'}" class="nav-link text-decoration-none text-light fw-bold">내 프로필</router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link @click.native="logout" to="#" class="nav-link text-decoration-none text-light fw-bold">로그아웃</router-link>
          </li>
        </ul>
        <ul v-else class="navbar-nav">
          <li class="nav-item mx-2">
            <router-link :to="{ name: 'Signup'}" class="nav-link text-decoration-none text-light fw-bold">회원가입</router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link :to="{ name: 'Login'}" class="nav-link text-decoration-none text-light fw-bold">로그인</router-link>
          </li>
        </ul>

      </div>
    </nav>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
    return {
      searchKeyword: null,
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
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
