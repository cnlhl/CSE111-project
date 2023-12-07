<template>
    <div class="attendance-meeting-container">
      <h1>Attendance to Meeting</h1>
      <table>
        <thead>
          <tr>
            <th>Theme</th>
            <th>Description</th>
            <th>Time</th>
            <th>Location</th>
            <th>Operation</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="meeting in meetings" :key="meeting.id">
            <td>{{ meeting.title }}</td>
            <td>{{ meeting.description }}</td>
            <td>{{ meeting.time }}</td>
            <td>{{ meeting.location }}</td>
            <td>
              <button v-if="meeting.status === 'pending'" @click="attendMeeting(meeting, true)">Attend</button>
              <button v-if="meeting.status === 'pending'" @click="attendMeeting(meeting, false)">Reject</button>
              <span v-else>{{ meeting.status === 'attended' ? 'Agreed' : 'Rejected' }}</span>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="goBack">goBack</button>
    </div>
  </template>
  
  <script>
  import { ref,onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import api from '@/api';
  
  export default {
    name: 'AttendanceMeeting',
    setup() {
      const router = useRouter();
      const meetings = ref([]);

      const fetchMeetings = async () => {
        try {
          const response = await api.getPendingMeetings();
          console.log('获取会议列表', response);
          meetings.value = response.data;
          console.log('meetings:', meetings);
        } catch (error) {
          console.error('获取会议列表失败', error);
        }
      };

      onMounted(fetchMeetings);
  
      const attendMeeting = async(meeting, willAttend) => {
        const status = willAttend ? 'attended' : 'rejected';
        const response = await api.updateMeetingStatus(meeting.meetingid,status);
        if(response.data.success){
          meeting.status = status;
        }else{
          console.error('更新会议状态失败');
        }
        console.log('会议状态更新', meeting);
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
    font-family: Arial, sans-serif;
    color: #333;
    background-color: #f5f5f5;
  }

  h1 {
    color: #4CAF50;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  button {
    margin: 10px 5px;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 1em;
    border-radius: 5px;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #45a049;
  }
  </style>