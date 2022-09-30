import Vue from "vue";
import Vuex from "vuex";

import { auth } from "./auth.module";
import { contact } from "./contact";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    contact,
  },
});
