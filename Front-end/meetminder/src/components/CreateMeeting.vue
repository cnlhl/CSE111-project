<template>
  <div class="create-meeting-container">
    <h1>Create Meeting</h1>
    <form @submit.prevent="submitMeeting">
      <div>
        <label for="title">Theme: </label>
        <input type="text" id="title" v-model="meeting.title">
      </div>
      <div>
        <label for="description">Description: </label>
        <textarea id="description" v-model="meeting.description"></textarea>
      </div>
      <div>
        <label for="time">Time: </label>
        <input type="datetime-local" id="time" v-model="meeting.time">
      </div>
      <div>
        <label for="location">Location: </label>
        <input type="text" id="location" v-model="meeting.location">
      </div>
      <div style="margin-bottom: 20px;">
        <label for="participants">Participants: </label>
        <VueMultiselect v-model="meeting.participants" :options="availableParticipants" :multiple="true"
          :searchable="true" :close-on-select="false" placeholder="Select Participants" label="username" track-by="userid"
          @search-change="asyncFindParticipants"></VueMultiselect>
      </div>
      <div style="margin-bottom: 20px;">
        <label for="resources">Resources: </label>
        <VueMultiselect v-model="meeting.resources" :options="availableResources" :multiple="true" :searchable="true"
          :close-on-select="false" placeholder="Select Resources" label="resourcename" track-by="resourceid"
          @search-change="asyncFindResources"></VueMultiselect>
      </div>
      <button type="submit" style="margin-bottom: 20px;">Create Meeting</button>
      <button @click="goBack">goBack</button>
    </form>
  </div>
  <div v-if="submitStatus" class="submit-status">{{ submitStatus }}</div>
</template>

<script>
import { ref,onMounted } from 'vue';
import { useRouter } from 'vue-router';
import VueMultiselect from 'vue-multiselect';
import api from '@/api';

export default {
  components: {
    VueMultiselect
  },
  name: 'CreateMeeting',
  setup() {
    const meeting = ref({
      title: '',
      description: '',
      time: '',
      location: '',
      participants: [],
      resources: []
    });

    const availableParticipants = ref([]);
    const availableResources = ref([]);
    const loading = ref(false);
    const errorMessage = ref('');

    const fetchInitialData = async () => {
      try {
        loading.value = true;
        const [participantsResponse, resourcesResponse] = await Promise.all([
          api.getParticipants(),
          api.getResources()
        ]);
        console.log('获取数据', participantsResponse, resourcesResponse);
        availableParticipants.value = participantsResponse.data;
        availableResources.value = resourcesResponse.data;
      } catch (error) {
        console.error('获取数据失败', error);
        errorMessage.value = 'Failed to fetch data';
      } finally {
        loading.value = false;
      }
    };

    onMounted(fetchInitialData);

    const router = useRouter();
    const submitStatus = ref('');

    const submitMeeting = async () => {
      try {
        const response = await api.createMeeting(meeting.value);
        if (response.data.success) {
          submitStatus.value = 'Meeting created successfully';
          router.push({ name: 'Home' });
        } else {
          // 创建失败，显示错误信息
          submitStatus.value = 'Failed to create meeting' + response.data.message;
        }
      } catch (error) {
        console.error('创建会议请求失败', error);
        submitStatus.value = 'Error: ' + error.message;
      }
    };

    const goBack = () => {
      router.push({ name: 'Home' });
    };

    return {
      meeting,
      submitMeeting,
      goBack,
      submitStatus,
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

.create-meeting-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #333;
  font-weight: bold;
}

input[type="text"],
input[type="datetime-local"],
textarea,
button {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.submit-status {
  color: red;
  margin-bottom: 20px;
}
</style>