import axios from "axios";

const instance = axios.create({
  baseURL: "http://0.0.0.0:8002/api/v1",
  // baseURL: "http://localhost:8080/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export default instance;
