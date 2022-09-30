import api from "./api";
import TokenService from "./token.service";

class ContactService {
  getContacts(query) {
 
    return api.get("/contact/",{ params: query}).then((response) => {
      if (response.data.access) {
        TokenService.setUser(response.data);
      }

      return response.data;
    });
  }
  getOneContact(id) {
    return api.get(`/contact/${id}/`).then((response) => {
      return response.data;
    });
  }

  updateContact({ id, data }) {
    return api.patch(`/contact/${id}/`, data).then((response) => {
      return response.data;
    });
  }

  createContact(data) {
    return api.post(`/contact/`, data).then((response) => {
      return response.data;
    });
  }

  deleteContact(id) {
    return api.delete(`/contact/${id}/`).then((response) => {
      return response.data;
    });
  }

  getTags() {
    return api.get("/tag/").then((response) => {
      return response.data;
    });
  }
}

export default new ContactService();
