<template>
    <div class="view-meeting-container">
      <h1>Meeting information</h1>
      <table>
        <thead>
          <tr>
            <th>Theme</th>
            <th>Description</th>
            <th>Time</th>
            <th>Location</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="meeting in meetings" :key="meeting.id">
            <td>
              <input v-if="editable" type="text" v-model="meeting.title">
              <span v-else>{{ meeting.title }}</span>
            </td>
            <td>
              <textarea v-if="editable" v-model="meeting.description"></textarea>
              <span v-else>{{ meeting.description }}</span>
            </td>
            <td>
              <input v-if="editable" type="datetime-local" v-model="meeting.time">
              <span v-else>{{ meeting.time }}</span>
            </td>
            <td>
              <input v-if="editable" type="text" v-model="meeting.location">
              <span v-else>{{ meeting.location }}</span>
            </td>
            <td>{{ meeting.role === 'Organizer' ? 'Organizer' : 'Participant' }}</td>
          </tr>
        </tbody>
      </table>
      <button @click="toggleEdit">{{ editable ? 'Save' : 'Manage' }}</button>
      <button @click="goBack">goBack</button>
    </div>
  </template>
  
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import api from '@/api';
  
  export default {
    name: 'ViewMeeting',
    setup() {
      const router = useRouter();
      const editable = ref(false);
      const loading = ref(false);
      const errorMessage = ref('');
      const meetings = ref([]);  // 使用 ref 而不是 reactive
  
      const fetchInitialData = async () => {
        try {
          loading.value = true;
          const response = await api.getMeetings();
          meetings.value = response.data;  // 更新 meetings
          console.log('meetings:', meetings.value);
        } catch (error) {
          console.error('获取会议数据失败', error);
          errorMessage.value = 'Failed to fetch data';
        } finally {
          loading.value = false;
        }
      };
  
      onMounted(fetchInitialData);
  
      const toggleEdit = async () => {
        editable.value = !editable.value;
        if (!editable.value) {
          try {
            const response = await api.updateMeeting(meetings.value);
            if (!response.data.success) {
              errorMessage.value = response.data.message || 'Failed to update meeting';
            }
          } catch (error) {
            console.error('更新会议信息失败', error);
            errorMessage.value = 'Error while updating meeting';
          }
        }
      };
  
      const goBack = () => {
        router.push({ name: 'Home' });
      };
  
      return { 
        meetings, 
        editable, 
        toggleEdit, 
        goBack, 
        loading, 
        errorMessage 
      };
    }
  };
  </script>
  

  
  <style scoped>
  @import 'vue-multiselect/dist/vue-multiselect.css';

  .view-meeting-container {
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

  input[type="text"], textarea, input[type="datetime-local"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-sizing: border-box;
  }
  </style>