
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/',
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
  async getUserData(userId) {
    const response = await apiClient.get(`/users/${userId}`);
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
  getMeetings() {
    return apiClient.get('/meetings');
  },
  updateMeeting(meeting) {
    return apiClient.put(`/meetings/${meeting.id}`, meeting);
  },
  getPendingMeetings() {
    return apiClient.get('/meetings/pending');
  },
  updateMeetingStatus(meetingId, status) {
    return apiClient.put(`/meetings/${meetingId}/status`, { status });
  },
  createResource(resource) {
    return apiClient.post('/resources', resource);
  },
  updateResource(resource) {
    return apiClient.put(`/resources/${resource.id}`, resource);
  },
  deleteResource(resourceId) {
    return apiClient.delete(`/resources/${resourceId}`);
  }
};
