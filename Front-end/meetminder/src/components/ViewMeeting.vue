<template>
    <div class="view-meeting-container">
      <h1>会议信息</h1>
      <table>
        <thead>
          <tr>
            <th>标题</th>
            <th>描述</th>
            <th>时间</th>
            <th>地点</th>
            <th>参与者</th>
            <th>资源</th>
            <th>会议角色</th>
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
                placeholder="选择参与者"
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
                placeholder="选择资源"
                label="name"
                track-by="name"
              ></VueMultiselect>
              <span v-else>{{ meeting.resources.join(', ') }}</span>
            </td>
            <td>{{ meeting.role === 'Organizer' ? '组织者' : '参与者' }}</td>
          </tr>
        </tbody>
      </table>
      <button @click="toggleEdit">{{ editable ? '保存' : '管理' }}</button>
      <button @click="goBack">返回</button>
    </div>
  </template>
  
  
  <script>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import VueMultiselect from 'vue-multiselect';

export default {
  components: {
    VueMultiselect
  },
  name: 'ViewMeeting',
  setup() {
    const router = useRouter();
    const editable = ref(false);
    const availableParticipants = ref([
      // ...这里是可选参与者的列表...
    ]);
    const availableResources = ref([
      // ...这里是可选资源的列表...
    ]);

    const meetings = reactive([
      // ...这里是会议的样本数据，实际应用中应从后端获取...
    ]);

    const toggleEdit = () => {
      editable.value = !editable.value;
      if (!editable.value) {
        console.log('保存会议信息', meetings);
        // 在这里添加保存逻辑，如发送到后端
      }
    };

    const goBack = () => {
      router.push({ name: 'Home' });
    };

    return { meetings, editable, toggleEdit, goBack, availableParticipants, availableResources };
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
  