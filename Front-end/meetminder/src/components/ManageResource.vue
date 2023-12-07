<template>
    <div class="manage-resource-container">
      <h1>Manage Resources</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th v-if="showRoomDetails">Room ID</th>
            <th v-if="showRoomDetails">Room Name</th>
            <th v-if="showRoomDetails">Capacity</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="resource in resources" :key="resource.id">
            <td>{{ resource.id }}</td>
            <td>
              <input v-if="editable" type="text" v-model="resource.name">
              <span v-else>{{ resource.name }}</span>
            </td>
            <td>
              <input v-if="editable" type="text" v-model="resource.description">
              <span v-else>{{ resource.description }}</span>
            </td>
            <template v-if="resource.description === 'room'">
              <td>
                <input v-if="editable" type="text" v-model="resource.roomID">
                <span v-else>{{ resource.roomID }}</span>
              </td>
              <td>
                <input v-if="editable" type="text" v-model="resource.roomname">
                <span v-else>{{ resource.roomname }}</span>
              </td>
              <td>
                <input v-if="editable" type="text" v-model="resource.capacity">
                <span v-else>{{ resource.capacity }}</span>
              </td>
            </template>
            <td>
              <button v-if="!resource.editing" @click="editResource(resource)">Edit</button>
              <button v-else @click="saveResource(resource)">Save</button>
              <button @click="deleteResource(resource)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="startAddingResource">Add New Resource</button>
      <button @click="goHome">Go Home</button>
    </div>
  </template>
  
  <script>
  import { ref, reactive, onMounted, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import api from '@/api';
  
  export default {
    name: 'ManageResource',
    setup() {
      const router = useRouter();
      const resources = reactive([]);
      const addingResource = ref(false);
      const newResource = ref({ name: '', type: '' });
  
      const fetchResources = async () => {
        try {
          const response = await api.getResources();
          resources.push(...response.data);
        } catch (error) {
          console.error('获取资源失败', error);
          // 错误处理
        }
      };
  
      onMounted(fetchResources);
  
      const editResource = (resource) => {
        resource.editing = true;
      };
      const showRoomDetails = computed(() => {
      return resources.some(resource => resource.description === 'room');
      });
  
      const saveResource = async (resource) => {
        try {
          const response = await api.updateResource(resource);
          if (response.data.success) {
            resource.editing = false;
          } else {
            // 错误处理
          }
        } catch (error) {
          console.error('保存资源失败', error);
          // 错误处理
        }
      };
  
      const deleteResource = async (resource) => {
        try {
          const response = await api.deleteResource(resource.id);
          if (response.data.success) {
            const index = resources.indexOf(resource);
            resources.splice(index, 1);
          } else {
            // 错误处理
          }
        } catch (error) {
          console.error('删除资源失败', error);
          // 错误处理
        }
      };
  
      const startAddingResource = () => {
        addingResource.value = true;
      };
  
      const addResource = async () => {
        try {
          const response = await api.createResource(newResource.value);
          if (response.data.success) {
            resources.push(response.data.resource);
            newResource.value = { name: '', type: '' };
            addingResource.value = false;
          } else {
            // 错误处理
          }
        } catch (error) {
          console.error('添加资源失败', error);
          // 错误处理
        }
      };
  
      const cancelAddingResource = () => {
        addingResource.value = false;
        newResource.value = { name: '', type: '' };
      };
  
      const goHome = () => {
        router.push({ name: 'Home' });
      };
  
      return { 
        resources, 
        addingResource, 
        newResource,
        editResource,
        saveResource,
        deleteResource,
        startAddingResource,
        addResource,
        cancelAddingResource,
        goHome,
        showRoomDetails
      };
    }
  };
  </script>
  
  <style scoped>
  .manage-resource-container {
    padding: 20px;
    text-align: center;
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
  
  th {
    background-color: #f4f4f4;
  }
  
  input[type="text"] {
    width: 100%;
    padding: 8px;
    margin: 5px 0;
    box-sizing: border-box;
  }
  
  button {
    margin: 5px;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  .add-new-row {
    text-align: right;
  }
  
  .add-new-row button {
    margin-top: 10px;
  }
  
  .error-message {
    color: red;
    margin: 10px 0;
  }
  </style>
  