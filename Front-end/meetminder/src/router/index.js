import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '@/components/Login'; // 确保路径正确

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
  ],
});

export default router;
