<template>
    <div class="create-meeting-container">
      <h1>创建会议</h1>
      <form @submit.prevent="submitMeeting">
        <div>
          <label for="title">标题：</label>
          <input type="text" id="title" v-model="meeting.title">
        </div>
        <div>
          <label for="description">描述：</label>
          <textarea id="description" v-model="meeting.description"></textarea>
        </div>
        <div>
          <label for="time">时间：</label>
          <input type="datetime-local" id="time" v-model="meeting.time">
        </div>
        <div>
          <label for="location">地点：</label>
          <input type="text" id="location" v-model="meeting.location">
        </div>
        <div>
      <label for="participants">参与者：</label>
      <VueMultiselect
        v-model="meeting.participants"
        :options="availableParticipants"
        :multiple="true"
        :searchable="true"
        :close-on-select="false"
        placeholder="选择参与者"
        label="name"
        track-by="name"
        @search-change="asyncFindParticipants"
      ></VueMultiselect>
    </div>
    <div>
      <label for="resources">资源：</label>
      <VueMultiselect
        v-model="meeting.resources"
        :options="availableResources"
        :multiple="true"
        :searchable="true"
        :close-on-select="false"
        placeholder="选择资源"
        label="name"
        track-by="name"
        @search-change="asyncFindResources"
      ></VueMultiselect>
    </div>
        <button type="submit" style="margin-bottom: 20px;">创建会议</button>
        <button @click="goBack">返回主页</button>
      </form>
    </div>
  </template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import VueMultiselect from 'vue-multiselect';

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

    const availableParticipants = ref([
      { name: '张三', id: 1 },
      { name: '李四', id: 2 },
      { name: '王五', id: 3 }
      // ...其他可选参与者...
    ]);

    const availableResources = ref([
      { name: '投影仪', id: 1 },
      { name: '白板', id: 2 },
      { name: '视频会议设备', id: 3 }
      // ...其他可选资源...
    ]);

    const router = useRouter();

    const submitMeeting = () => {
      console.log('会议详情', meeting.value);
      // 实现提交会议的逻辑，可能包括与后端的通信
    };

    const goBack = () => {
      router.push({ name: 'Home' });
    };

    // 异步搜索参与者的方法，根据需求实现
    const asyncFindParticipants = async (query) => {
        console.log('搜索参与者', query);
      // 例如从服务器获取匹配的参与者列表
      // 更新 availableParticipants.value
    };

    // 异步搜索资源的方法，根据需求实现
    const asyncFindResources = async (query) => {
        console.log('搜索资源', query);
      // 例如从服务器获取匹配的资源列表
      // 更新 availableResources.value
    };

    return { 
      meeting, 
      submitMeeting, 
      goBack, 
      availableParticipants, 
      availableResources,
      asyncFindParticipants,
      asyncFindResources
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
    }
    input[type="text"],
    input[type="datetime-local"],
    textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 20px;
    }
    button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
  </style>