import axios from "axios";

// Create an axios instance
const instance = axios.create({
    baseURL: "http://api.amirshokh.live/api/v1",
    // baseURL: "http://localhost:8080/api",
    headers: {
        "Content-Type": "application/json",
    },
});

export default instance;
