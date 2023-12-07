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
            <th>Participants</th>
            <th>Resources</th>
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
            <td>
              <VueMultiselect
                v-if="editable"
                v-model="meeting.participants"
                :options="availableParticipants"
                :multiple="true"
                placeholder="Select Participants"
                label="name"
                track-by="name"
              ></VueMultiselect>
              <span v-else>{{ meeting.participants.join(', ') }}</span>
            </td>
            <td>
              <VueMultiselect
                v-if="editable"
                v-model="meeting.resources"
                :options="availableResources"
                :multiple="true"
                placeholder="Select Resources"
                label="name"
                track-by="name"
              ></VueMultiselect>
              <span v-else>{{ meeting.resources.join(', ') }}</span>
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
import { ref, reactive,onMounted } from 'vue';
import { useRouter } from 'vue-router';
import VueMultiselect from 'vue-multiselect';
import api from '@/api';

export default {
  components: {
    VueMultiselect
  },
  name: 'ViewMeeting',
  setup() {
    const router = useRouter();
    const editable = ref(false);
    const availableParticipants = ref([]);
    const availableResources = ref([]);
    const loading = ref(false);
    const errorMessage = ref('');

    const fetchInitialData = async () => {
      try {
        loading.value = true;
        const [meetingsResponse, participantsResponse, resourcesResponse] = await Promise.all([
          api.getMeetings(),
          api.getParticipants(),
          api.getResources()
        ]);
        meetings.value = meetingsResponse.data;
        availableParticipants.value = participantsResponse.data;
        availableResources.value = resourcesResponse.data;
      } catch (error) {
        console.error('获取会议数据失败', error);
        errorMessage.value = 'Failed to fetch data';
      } finally {
        loading.value = false;
      }
    };

    onMounted(fetchInitialData);

    const meetings = reactive([
      // ...这里是会议的样本数据，实际应用中应从后端获取...
    ]);

    const toggleEdit = async() => {
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
      availableParticipants, 
      availableResources,
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
  