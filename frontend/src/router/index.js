import { createRouter, createWebHistory } from "vue-router";
import Candidate from "../components/Candidate.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/candidates",
      name: "Candidates",
      component: Candidate
    }
  ],
});

export default router;
