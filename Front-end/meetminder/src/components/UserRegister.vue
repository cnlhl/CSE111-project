<template>
    <div class="register-container">
      <div class="register-box">
        <h1 class="register-title">Register</h1>
        <form @submit.prevent="register" class="register-form">
          <div class="form-group">
            <input type="text" id="username" v-model="username" placeholder="Username">
          </div>
          <div class="form-group">
            <input type="email" id="email" v-model="email" placeholder="Email">
          </div>
          <div class="form-group">
            <input type="password" id="password" v-model="password" placeholder="Password">
          </div>
          <div class="form-group">
            <input type="password" id="confirmPassword" v-model="confirmPassword" placeholder="Confirm Password">
          </div>
          <button type="submit" class="register-button">Register</button>
        </form>
        <p v-if="registrationError" class="error-message">{{ registrationError }}</p>
        <p v-if="registrationSuccess" class="success-message">
          Registration successful.
          <router-link to="/login">Go to login</router-link>
        </p>
        <router-link to="/login" class="back-to-login">Back to Login</router-link>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import api from '@/api'; // 确保已正确导入 api
  
  export default {
    name: 'UserRegister',
    setup() {
      const username = ref('');
      const email = ref('');
      const password = ref('');
      const confirmPassword = ref('');
      const registrationError = ref('');
      const registrationSuccess = ref(false);
  
      const register = async () => {
        if (password.value !== confirmPassword.value) {
          registrationError.value = 'Passwords do not match.';
          return;
        }
  
        try {
          const user = {
            username: username.value,
            email: email.value,
            password: password.value
          };
          const response = await api.createUsers(user);
          if (response.data.success) {
            registrationSuccess.value = true;
            registrationError.value = '';
          } else {
            registrationError.value = response.data.message || 'Registration failed.';
            registrationSuccess.value = false;
          }
        } catch (error) {
          registrationError.value = error.message || 'Registration failed.';
          registrationSuccess.value = false;
        }
      };
  
      return {
        username,
        email,
        password,
        confirmPassword,
        register,
        registrationError,
        registrationSuccess
      };
    }
  };
  </script>
  
  
  <style scoped>
  .register-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f7f7f7;
  }

  .back-to-login {
  display: block;
  text-align: center;
  margin-top: 1rem;
  color: #333;
  text-decoration: none;
}

  
  .register-box {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 400px;
  }
  
  .register-title {
    text-align: center;
    margin-bottom: 2rem;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 1rem;
    border-radius: 4px;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }
  
  input::placeholder {
    color: #aaa;
  }
  
  .register-button {
    width: 100%;
    padding: 1rem;
    border-radius: 4px;
    border: none;
    background-color: #5cb85c;
    color: white;
    cursor: pointer;
    font-size: 1rem;
    margin-top: 1rem;
  }
  
  .register-button:hover {
    background-color: #4cae4c;
  }
  
  .error-message,
  .success-message {
    text-align: center;
    margin-top: 1rem;
  }
  
  .success-message a {
    color: #5cb85c;
    text-decoration: none;
    font-weight: bold;
  }
  </style>
  