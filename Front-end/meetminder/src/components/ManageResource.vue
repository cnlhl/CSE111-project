<template>
    <div class="manage-resource-container">
      <h1>Manage Resources</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="resource in resources" :key="resource.id">
            <td v-if="!resource.editing">{{ resource.name }}</td>
            <td v-else><input type="text" v-model="resource.name" /></td>
  
            <td v-if="!resource.editing">{{ resource.type }}</td>
            <td v-else><input type="text" v-model="resource.type" /></td>
  
            <td>
              <button v-if="!resource.editing" @click="editResource(resource)">Edit</button>
              <button v-else @click="saveResource(resource)">Save</button>
              <button @click="deleteResource(resource)">Delete</button>
            </td>
          </tr>
          <tr v-if="addingResource">
            <td><input type="text" v-model="newResource.name" /></td>
            <td><input type="text" v-model="newResource.type" /></td>
            <td>
              <button @click="addResource">Add</button>
              <button @click="cancelAddingResource">Cancel</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="startAddingResource">Add New Resource</button>
      <button @click="goHome">Go Home</button>
    </div>
  </template>
  
  <script>
  import { ref, reactive, onMounted } from 'vue';
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
        goHome
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
  