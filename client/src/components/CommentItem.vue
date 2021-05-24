<template>
  <div>
    <div v-if="isClicked">
      <label for="content">댓글 내용: </label>
      <input type="text" id="content" v-model="newComment" @keyup.enter="updateComment">
      <button @click="updateComment">댓글 저장</button>
    </div>
    <div v-else>
      <span>{{ comment.content }}</span>
      <br>
      <span>작성 시간: {{ comment.created_at }}</span>
      <!--수정되었을 경우에만 수정 시간을 보여준다. -->
      <span v-if="comment.created_at !== comment.updated_at">수정 시간: {{ comment.updated_at }}</span>
      <button v-if="requestUser.id === comment.user" @click="makeInput">댓글 수정</button>
    </div>
    <button v-if="requestUser.id === comment.user" @click="deleteComment">댓글 삭제</button> 
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentItem',
  data: function () {
    return {
      isClicked: false,
      newComment: this.comment.content
    }
  },
  props: {
    comment: {
      type: Object
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    // updateComment: function () {
    
    // },
    deleteComment: function () {
      axios({
        url: 'http://127.0.0.1:8000/movies/comments/' + this.comment.id +'/',
        method: 'delete',
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('delete-comment')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    makeInput: function () {
      this.isClicked= true
    },
    updateComment:  function () {
      axios({
        url: 'http://127.0.0.1:8000/movies/comments/' + this.comment.id +'/',
        method: 'put',
        data: {
          content: this.newComment
        },
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$emit('update-comment')
          // 다시 댓글들이 보이도록
          this.isClicked= false
        })
        .catch((err) => {
          console.log(err)
        })
    }, 
  },
  computed: {
    requestUser: function () {
      return this.$store.state.userinfo
    }
  },
}
</script>

<style>

</style>