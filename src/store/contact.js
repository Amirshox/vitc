import ContactService from "../services/contacts";

export const contact = {
    namespaced: true,
    state: {
        contact: [],
        tags: [],
        one_contact: {},
    },

    getters: {
        GET_CONTACTS: (state) => state.contact,
        GET_ONE_CONTACT: (state) => state.one_contact,
        GET_TAGS: (state) => state.tags,
    },

    actions: {
        FETCH_CONTACTS({state}, params) {
            return ContactService.getContacts(params).then(
                (res) => {
                    // console.log(res)
                    state.contact = res;
                    return Promise.resolve();
                },
                (error) => {
                    return Promise.reject(error);
                }
            );
        },

        FETCH_ONE_CONTACT({state}, id) {
            return ContactService.getOneContact(id).then(
                (res) => {
                    state.one_contact = res;
                    return Promise.resolve();
                },
                (error) => {
                    return Promise.reject(error);
                }
            );
        },

        UPDATE_CONTACT(_, data) {
            return ContactService.updateContact(data);
        },
        CREATE_CONTACT(_, data) {
            return ContactService.createContact(data);
        },
        DELETE_CONTACT(_, id) {
            return ContactService.deleteContact(id);
        },

        FETCH_TAGS({state}) {
            return ContactService.getTags().then(
                (res) => {
                    // console.log(res)
                    state.tags = res;
                    return Promise.resolve();
                },
                (error) => {
                    return Promise.reject(error);
                }
            );
        },
    },
};
