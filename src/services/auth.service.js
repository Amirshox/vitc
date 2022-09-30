import api from "./api";
import TokenService from "./token.service";

class AuthService {
  login({ username, password }) {
    return api
      .post("/token/", {
        username,
        password,
      })
      .then((response) => {
        console.log("response", response);
        if (response.data.access) {
          TokenService.setUser(response.data);
        }

        return response.data;
      });
  }

  logout() {
    TokenService.removeUser();
  }

  register({ username, password }) {
    return api.post("/user/", {
      username,
      password,
    });
  }
}

export default new AuthService();
