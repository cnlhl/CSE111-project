import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 确保这个路径与你的路由配置文件相匹配

const app = createApp(App);
app.use(router); // 使用路由器
app.mount('#app');