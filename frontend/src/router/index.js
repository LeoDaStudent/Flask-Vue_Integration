import Vue from "vue";
import VueRouter from "vue-router";
import CandidatesView from "../components/candidatesView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/candidates",
    name: "candidates",
    component: CandidatesView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
