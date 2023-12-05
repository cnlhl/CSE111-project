<template>
    <div class="attendance-meeting-container">
      <h1>参加会议</h1>
      <table>
        <thead>
          <tr>
            <th>标题</th>
            <th>描述</th>
            <th>时间</th>
            <th>地点</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="meeting in meetings" :key="meeting.id">
            <td>{{ meeting.title }}</td>
            <td>{{ meeting.description }}</td>
            <td>{{ meeting.time }}</td>
            <td>{{ meeting.location }}</td>
            <td>
              <button v-if="meeting.status === 'pending'" @click="attendMeeting(meeting, true)">出席</button>
              <button v-if="meeting.status === 'pending'" @click="attendMeeting(meeting, false)">拒绝</button>
              <span v-else>{{ meeting.status === 'attended' ? '已出席' : '已拒绝' }}</span>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="goBack">返回</button>
    </div>
  </template>
  
  <script>
  import { reactive } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'AttendanceMeeting',
    setup() {
      const router = useRouter();
      const meetings = reactive([
        // 这里是样本数据，实际应用中应从后端获取
        { id: 1, title: '会议1', description: '描述1', time: '2023-10-10T10:00', location: '地点1', status: 'pending' },
        { id: 2, title: '会议2', description: '描述2', time: '2023-10-11T11:00', location: '地点2', status: 'pending' }
        // ...更多会议
      ]);
  
      const attendMeeting = (meeting, willAttend) => {
        meeting.status = willAttend ? 'attended' : 'rejected';
        console.log('会议状态更新', meeting);
        // 这里添加发送状态更新到后端的逻辑
      };
  
      const goBack = () => {
        router.push({ name: 'Home' });
      };
  
      return { meetings, attendMeeting, goBack };
    }
  };
  </script>
  
  <style scoped>
    .attendance-meeting-container {
      padding: 20px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    button {
      margin: 10px 5px;
      padding: 10px;
    }
  </style>
  