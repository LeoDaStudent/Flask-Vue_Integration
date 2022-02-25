import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
// Importing the bootstrapvue library
import BootstrapVue from "bootstrap-vue";

const app = createApp(App);

app.use(router);
app.use(BootstrapVue);

app.mount("#app");
