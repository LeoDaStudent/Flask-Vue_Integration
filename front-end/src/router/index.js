import Vue from "vue";
import VueRouter from "vue-router";
import Canidate from "@/components/Canidate";

Vue.use(VueRouter);

const routes = [
  {
    path: "/candidates",
    name: "Candidates",
    component: Canidate
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
