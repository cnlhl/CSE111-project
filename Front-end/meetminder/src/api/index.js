
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://your-backend-url',
  withCredentials: false, // 根据你的设置调整
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  loginUser(username, password) {
    const response = apiClient.post('/login', { username, password });
    return response.data;
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
  }
};
