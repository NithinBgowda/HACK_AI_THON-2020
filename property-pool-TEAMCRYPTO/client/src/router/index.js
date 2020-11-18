import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/u/:id",
    name: "user",
    component: () => import("@/views/User"),
  },
  {
    path: "/p/:tokenId",
    name: "property",
    component: () => import("@/views/Property"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
