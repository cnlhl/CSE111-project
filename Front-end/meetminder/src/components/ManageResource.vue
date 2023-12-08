<template>
  <div class="manage-resource-container">
    <h1>Manage Resources</h1>
    <input type="text" v-model="searchTerm" placeholder="Search by Resource Name" style="width: 200px; float: left;">
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Description</th>
          <th v-if="showRoomDetails">Room ID</th>
          <th v-if="showRoomDetails">Room Name</th>
          <th v-if="showRoomDetails">Capacity</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="resource in filteredResources" :key="resource.resourceid">
          <td>{{ resource.resourceid }}</td>
          <td>
            <input v-if="resource.editing" type="text" v-model="resource.resourcename">
            <span v-else>{{ resource.resourcename }}</span>
          </td>
          <td>
            <input v-if="resource.editing" type="text" v-model="resource.description">
            <span v-else>{{ resource.description }}</span>
          </td>
          <template v-if="resource.description === 'Room'">
            <td>
              <input v-if="resource.editing" type="text" v-model="resource.roomid" readonly>
              <span v-else>{{ resource.roomid }}</span>
            </td>
            <td>
              <input v-if="resource.editing" type="text" v-model="resource.roomname">
              <span v-else>{{ resource.roomname }}</span>
            </td>
            <td>
              <input v-if="resource.editing" type="text" v-model="resource.capacity">
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
    <button @click="addResource">Add</button>
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
    const searchTerm = ref('');

    const filteredResources = computed(() => {
      if (!searchTerm.value) {
        return resources;
      }
      return resources.filter(resource =>
        resource.resourcename.toLowerCase().includes(searchTerm.value.toLowerCase())
      );
    });

    const fetchResources = async () => {
  try {
    const response = await api.getResources();
    const roomResponse = await api.getRooms();
    const roomMap = new Map(roomResponse.data.map(room => [room.resourceid, room]));

    response.data.forEach(resource => {
      resource.editing = false;
      // 假设 resource 对象中有一个 resourceid 字段
      const roomInfo = roomMap.get(resource.resourceid);
      if (roomInfo) {
        // 添加房间信息到资源对象中
        resource.roomid = roomInfo.roomid;
        resource.roomname = roomInfo.name;
        resource.capacity = roomInfo.capacity;
      }
    });

    resources.push(...response.data);
    console.log('获取资源', resources);
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
      return resources.some(resource => resource.description === 'Room');
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
        const response = await api.deleteResource(resource.resourceid);
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

    const addResource = async () => {
      addingResource.value = true;
      resources.push({
        resourceid: '',
        resourcename: '',
        description: '',
        roomid: '',
        roomname: '',
        capacity: '',
        editing: true
      });
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
      addResource,
      cancelAddingResource,
      goHome,
      showRoomDetails,
      searchTerm,
      filteredResources,
    };
  }
};
</script>
  
<style scoped>
.manage-resource-container {
  padding: 20px;
  text-align: center;
  width: 90%; /* 设置容器宽度为90%，使得左右两边有一定的空白 */
  margin: auto; /* 自动设置左右边距，使得容器在页面中居中 */
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  font-size: 1.2em; /* 增大字体大小 */
}

th,
td {
  border: 1px solid #ddd;
  padding: 4px; /* 减小单元格内边距 */
  text-align: left;
  vertical-align: middle;
}

th {
  background-color: #4CAF50;
  /* 更改为与按钮相同的颜色 */
  color: white;
  /* 文字颜色为白色 */
}

input[type="text"] {
  width: calc(100% - 16px);
  /* 减去内边距的宽度 */
  padding: 8px;
  margin: 4px 0;
  box-sizing: border-box;
  border-radius: 4px;
  /* 圆角 */
  border: 1px solid #ccc;
}

button {
  margin: 5px;
  padding: 8px 15px;
  /* 统一内边距 */
  min-width: 100px;
  /* 最小宽度 */
  height: 40px;
  /* 统一高度 */
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s, box-shadow 0.3s;
}

button:hover {
  background-color: #45a049;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* 添加此样式以避免输入框和按钮在同一行时对齐问题 */
input[type="text"],
input[type="email"],
input[type="password"] {
  width: calc(100% - 20px);
  /* 减去边距和边框的宽度 */
  /* 其他样式保持不变 */
}

.empty-cell {
  background-color: #fafafa;
  /* 空单元格的背景颜色 */
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

.success-message {
  color: #28a745;
  margin: 10px 0;
}

th:last-child,
td:last-child {
  width: 120px;
  /* 调整为实际需要的宽度 */
}</style>
  
  