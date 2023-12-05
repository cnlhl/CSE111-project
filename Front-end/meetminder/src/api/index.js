import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://your-backend-api-url', // 替换为你的后端 API 地址
  // 可以添加更多配置，如 headers 等
});

export default instance;
