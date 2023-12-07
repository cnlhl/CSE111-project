<template>
    <div class="home-container">
      <h1>Meetminder</h1>
      <div class="user-status">
        <p>Username: {{ userData.value.username }}</p>
        <p>Current Time: {{ currentTime }}</p>
        <p>Next Meeting: {{ userData.value.nextMeetingTime }}</p>
        <p>Meetings to Attend: {{ userData.value.meetingsToAttend }}</p>
      </div>
      <div class="action-bar">
        <button @click="createMeeting">Create Meeting</button>
        <button @click="viewMeeting">View Meeting</button>
        <button @click="attendMeeting">Attendance to Meeting</button>
      </div>
      <div class="notification-bar">
        <h2>Notification</h2>
        <p>{{ userData.latestNotification }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  
  export default {
    name: 'HomePage',
    setup() {
      const route = useRoute();
      const userData = ref({
        username: 'Guest',
        nextMeetingTime: '',
        meetingsToAttend: 0,
        latestNotification: ''
      });
  
      onMounted(() => {
        if (route.params) {
          userData.value = { ...route.params };
        }
  
        // 更新当前时间
        const currentTime = ref(new Date().toLocaleTimeString());
        setInterval(() => {
          currentTime.value = new Date().toLocaleTimeString();
        }, 1000);
  
        return { userData, currentTime };
      });
    }
  };
  </script>
  
  <style scoped>
  .home-container {
    padding: 20px;
    text-align: center;
  }
  .user-status p, .notification-bar p {
    margin: 10px 0;
  }
  .action-bar button {
    margin: 5px;
    padding: 10px;
  }
  </style>
  