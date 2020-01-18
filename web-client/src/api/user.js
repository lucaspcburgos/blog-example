import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:5000/user"
});

export default {
  auth: {
    userLogin(payload) {
      return apiClient.post("/auth/login/", payload);
    }
  },
  profile: {
    userSignup(payload) {
      return apiClient.post("/signup", payload);
    }
  }
};
