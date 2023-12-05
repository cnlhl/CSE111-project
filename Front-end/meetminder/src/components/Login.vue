<template>
  <div class="login-container">
    <h1>Meetminder</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">用户名：</label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">密码：</label>
        <input type="password" id="password" v-model="password">
      </div>
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UserLogin', // 改为多单词的组件名称
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // 登录逻辑
      console.log('登录', this.username, this.password);
    }
  }
};
</script>

<style scoped>
  .login-container {
    max-width: 300px;
    margin: 0 auto;
    padding: 20px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 20px;
  }
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
</style>
