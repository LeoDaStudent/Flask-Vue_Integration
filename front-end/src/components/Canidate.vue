<template>
  <table class="table table-striped">
    <thead class="thead-light">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Points</th>
        <th scope="col">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(person, index) in candidates" :key="index">
        <th scope="row">{{ person.id }}</th>
        <th scope="row">{{ person.name }}</th>
        <th scope="row">{{ person.points }}</th>
        <th scope="row">
          <div class="btn-group" role="group">
            <button class="btn btn-primary px-3">
              <i class="fab fa-android" aria-hidden="true"></i>
            </button>
            <button type="button" class="btn btn-danger btn-sm">Delete</button>
          </div>
        </th>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      candidates: [],
    };
  },
  methods: {
    getCandidates() {
      const path = "http://localhost:5000/candidates";
      axios
        .get(path)
        .then((res) => {
          this.candidates = res.data.candidates;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getCandidates();
  },
};
</script>

<style scoped></style>
