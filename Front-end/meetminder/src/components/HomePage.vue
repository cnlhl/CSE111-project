<template>
    <div class="home-container">
      <h1>Meetminder</h1>
      <div class="user-status">
        <p>用户名：Sample User</p>
        <p>当前时间：{{ currentTime }}</p>
        <p>下一场会议时间：14:00</p>
        <p>须参加的会议数量：3</p>
      </div>
      <div class="action-bar">
        <button @click="createMeeting">Create Meeting</button>
        <button @click="viewMeeting">View Meeting</button>
        <button @click="attendMeeting">Attendance to Meeting</button>
      </div>
      <div class="notification-bar">
        <h2>通知栏</h2>
        <p>最新通知：会议室地点变更至303室</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  export default {
    name: 'HomePage',
    setup() {
        
      const currentTime = ref(new Date().toLocaleTimeString());
      const router = useRouter();
  
      onMounted(() => {
        setInterval(() => {
          currentTime.value = new Date().toLocaleTimeString();
        }, 1000);
      });
  
      const createMeeting = () => {
        console.log('创建会议');
        router.push({ name: 'CreateMeeting' });
        // 此处添加创建会议的逻辑
      };
  
      const viewMeeting = () => {
        console.log('管理会议');
        router.push({ name: 'ViewMeeting' });
        // 此处添加管理会议的逻辑
      };
  
      const attendMeeting = () => {
        console.log('参加会议');
        router.push({ name: 'AttendanceMeeting' });
        // 此处添加参加会议的逻辑
      };
  
      return { currentTime, createMeeting, viewMeeting, attendMeeting };
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
  