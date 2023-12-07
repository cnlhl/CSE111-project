<template>
  <div class="home-container">
    <h1>Meetminder</h1>
    <div class="user-status">
      <p>Username: {{ userData.username }}</p>
      <p>Current Time: {{ currentTime }}</p>
      <p>Next Meeting: {{ userData.nextMeetingTime }}</p>
      <p>Meetings to Attend: {{ userData.meetingsToAttend }}</p>
    </div>
    <div class="action-bar">
      <button @click="createMeeting">Create Meeting</button>
      <button @click="viewMeeting">View Meeting</button>
      <button @click="attendMeeting">Attendance to Meeting</button>
      <button @click="manageResource">Manage Resources</button>
    </div>
    <div class="notification-bar">
      <h2>Notification</h2>
      <p>{{ userData.latestNotification }}</p>
    </div>
  </div>
</template>
  
<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api';

// 在 setup 函数外部声明 currentTime 并导出
const currentTime = ref(new Date().toLocaleTimeString());

export default {
  name: 'HomePage',
  props: {
    userId: Number,
    username: String
  },
  setup(props) {
    const route = useRouter();
    const userData = ref({
      username: 'Guest',
      nextMeetingTime: '',
      meetingsToAttend: 0,
      latestNotification: ''
    });

    const getCurrentUserData = async () => {
      try {
        // 向后端发送请求获取数据
        const response = await api.getUserData(props.userId); // 假设你的 API 方法是 getUserData，接收 userID 参数
        // 更新 userData 对象的值
        console.log('获取用户数据', response);
        userData.value = {
          username: response.data.username,
          nextMeetingTime: response.data.nextMeeting,
          meetingsToAttend: response.data.meetingsToAttend,
          latestNotification: response.data.latestNotification
        };
      } catch (error) {
        console.error('获取用户数据失败', error);
      }
    };
    onMounted(() => {
      // 更新当前时间
      getCurrentUserData();
      setInterval(() => {
        currentTime.value = new Date().toLocaleTimeString();
      }, 1000);
    });

    const manageResource = () => {
      route.push({ name: 'ManageResource' });
    };

    const createMeeting = () => {
      route.push({ name: 'CreateMeeting' });
    };

    const viewMeeting = () => {
      route.push({ name: 'ViewMeeting' });
    };

    const attendMeeting = () => {
      route.push({ name: 'AttendanceMeeting' });
    };

    return {
      userData,
      manageResource,
      createMeeting,
      viewMeeting,
      attendMeeting,
      // 导出 currentTime，使其在整个组件中可用
      currentTime
    };
  }
};
</script>
  

<style scoped>
.home-container {
  padding: 20px;
  text-align: center;
  font-family: Arial, sans-serif;
  color: #333;
  background-color: #f5f5f5;
}

h1 {
  color: #4CAF50;
}

.user-status p,
.notification-bar p {
  margin: 10px 0;
  font-size: 1.2em;
}

.action-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.action-bar button {
  margin: 5px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 1em;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.action-bar button:hover {
  background-color: #45a049;
}

.notification-bar {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
  