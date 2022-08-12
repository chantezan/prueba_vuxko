<template>
  <form action="/loginuser/" method="POST">
  <label for="user">user</label>
  <input type="text" :value="user" id="user" name="username">
  <label for="pass">pass</label>
  <input type="text" :value="pass" id="pass" name="password">
  <button>logear</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  name: 'BaseLogin',
  data(){
    return {
      user: '',
      pass: ''
    }
  },
  methods: {
    log() {
      axios.post('/loginuser/', {
        username: this.user,
        password: this.pass,

    }, {
      withCredentials: true,
      headers: {
      'Content-Type': 'application/json',
      },
    })

    .then(function (response) {
      console.log(response)
    }.bind(this))
    },

  }
}
</script>

<style scoped>

</style>