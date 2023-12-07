<template>
  <div class="login-container">
    <h1>Meetminder</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username: </label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">Password: </label>
        <input type="password" id="password" v-model="password">
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="loginError" class="error-message">Username/Password incorrect</p>
    <p class="register-link">New user? <router-link to="/register">Register here</router-link></p>
  </div>
  <p v-if="loginError" class="error-message">Username/Password incorrect</p>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api';

export default {
  name: 'UserLogin',
  setup() {
    const router = useRouter();
    const username = ref('');
    const password = ref('');
    const loginError = ref(false);

    const login = async () => {
      try {
        const response = await api.loginUser(username.value,password.value);
        
        if (response.data.success) {
          // 成功登录，更新主页信息并跳转
          router.push({ name: 'Home', params: response });
        } else {
          // 显示错误信息
          loginError.value = true;
        }
      } catch (error) {
        console.error('登录请求失败', error);
      }
    };

    return { username, password, login, loginError };
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
