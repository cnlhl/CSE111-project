import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '@/components/Login'; // 确保路径正确
import HomePage from '@/components/HomePage';
import CreateMeeting from '@/components/CreateMeeting.vue';
import ViewMeeting from '@/components/ViewMeeting.vue';
import AttendanceMeeting from '@/components/AttendanceMeeting.vue';
import UserRegister from '@/components/UserRegister.vue';

// 创建路由器实例
const router = createRouter({
  history: createWebHistory(), // 使用 HTML5 History 路由模式
  routes: [
    {
      path: '/login',
      name: 'UserLogin',
      component: UserLogin
    },
    // 其他路由...
    {
      path: '/home',
      name: 'Home',
      component: HomePage
    },
    {
      path: '/create-meeting',
      name: 'CreateMeeting',
      component: CreateMeeting
    },
    {
      path: '/view-meeting',
      name: 'ViewMeeting',
      component: ViewMeeting
    },
    {
      path: '/attendance-meeting',
      name: 'AttendanceMeeting',
      component: AttendanceMeeting
    },
    {
      path: '/register',
      name: 'Register',
      component: UserRegister
    }
  ],
});

export default router;
