import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import AddEditContact from "./views/AddEditContact";

Vue.use(Router);

export const router = new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
        },
        {
            path: "/home",
            component: Home,
        },
        {
            path: "/login",
            component: Login,
        },
        {
            path: "/register",
            component: Register,
        },

        {
            path: "/home/add-contact",
            component: AddEditContact,
        },
        {
            path: "/home/edit-contact/:id",
            component: AddEditContact,
        },
    ],
});

router.beforeEach((to, from, next) => {
    const publicPages = ["/login", "/register", "/home"];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem("user");

    // trying to access a restricted page + not logged in
    // redirect to login page
    if (authRequired && !loggedIn) {
        next("/login");
    } else {
        next();
    }
});
