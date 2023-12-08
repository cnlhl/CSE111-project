
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000/',
  withCredentials: false, // 根据你的设置调整
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
 async loginUser(username, password) {
    const response = await apiClient.post('/login', { username, password });
    return response;
  },
  async getUserData() {
    const response = await apiClient.get(`/users`);
    return response;
  },
  getParticipants() {
    return apiClient.get('/participants');
  },
  getResources() {
    return apiClient.get('/resources');
  },
  createMeeting(meeting) {
    return apiClient.post('/meetings', meeting);
  },
  async getMeetings() {
    return apiClient.get('/meetings');
  },
  updateMeeting(meeting) {
    return apiClient.post(`/updatemeetings`, meeting);
  },
  getPendingMeetings() {
    return apiClient.get('/meetings/pending');
  },
  updateMeetingStatus(meetingId, status) {
    return apiClient.post(`/updateattendance`, { meetingId,status });
  },
  createResource(resource) {
    return apiClient.post('/resources', resource);
  },
  updateResource(resource) {
    return apiClient.put(`/updateresources`, resource);
  },
  deleteResource(resourceid) {
    return apiClient.delete(`/deleteresources/${resourceid}`);
  },
  createUsers(user) {
    return apiClient.post('/register', user);
  },
  async getRooms() {
    return apiClient.get(`/rooms`);
  },
  deleteMeeting(meetingId) {
    return apiClient.delete(`/deletemeetings/${meetingId}`);
  }
};
