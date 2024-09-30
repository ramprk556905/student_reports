import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/',  // Adjust based on your FastAPI server
});

export default api;
