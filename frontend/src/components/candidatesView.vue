<template>
  <!--  Display candidate table-->
  <div id="Main page">
    <table class="table table-striped">
      <thead class="thead-dark">
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
              <button
                class="btn btn-warning px-3"
                @click="upvoteCandidate(person)"
              >
                <font-a icon="arrow-up" />
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="deleteCandidate(person)"
              >
                Delete
                <font-a icon="dumpster" />
              </button>
            </div>
          </th>
        </tr>
      </tbody>
    </table>

    <!-- ADD button  -->
    <div>
      <button
        type="button"
        class="btn btn-primary btn-lg"
        v-b-modal.candidate-modal
      >
        Add Candidate
      </button>
    </div>

    <!-- Modal 1 -->
    <b-modal
      ref="addCandidateModal"
      id="candidate-modal"
      title="Add a new candidate"
      hide-backdrop
      hide-footer
    >
      <b-form @submit="onSubmit" class="w-100">
        <b-form-group id="form-id-group" label="ID:" label-for="form-id-input">
          <b-form-input
            id="form-id-input"
            type="number"
            v-model="addCandidateForm.id"
            required
            placeholder="Enter ID # Now"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-name-group"
          label="Name:"
          label-for="form-name-input"
        >
          <b-form-input
            id="form-name-input"
            type="text"
            v-model="addCandidateForm.name"
            required
            placeholder="Enter Name"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-points-group"
          label="Points"
          label-for="form-points-group"
        >
          <b-form-input
            id="form-points-group"
            type="number"
            v-model="addCandidateForm.points"
            required
            placeholder="# of Points"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="outline-info">Submit</b-button>
      </b-form>
    </b-modal>
    <!--  Enf of Modal 1 Add Candidate -->
  </div>
  <!--  End of page -->
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      candidates: [],
      addCandidateForm: {
        id: null,
        name: "",
        points: null,
      },
    };
  },
  methods: {
    // 1 - Get request to backend to get all candidates
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
    // 2 - Put request to backend to create new candidate
    addCandidate(payload) {
      const path = "http://localhost:5000/candidates";
      axios
        .post(path, payload)
        .then(() => {
          this.getCandidates();
          // for message alert
          this.message = "Ard ... bet";
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getCandidates();
        });
    },
    // 3 - Handles the submit button on Modal 1 (add candidate)
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addCandidateModal.hide();
      const payload = {
        id: this.addCandidateForm.id,
        name: this.addCandidateForm.name,
        points: this.addCandidateForm.points,
      };
      this.addCandidate(payload);
      this.clearForm();
    },
    //4 - Clears form
    clearForm() {
      this.addCandidateForm.id = null;
      this.addCandidateForm.name = "";
      this.addCandidateForm.points = null;
    },
    // 5 - Delete candidate
    removeCandidate(candidateID) {
      const path = `http://localhost:5000/candidates/${candidateID}`;
      axios
        .delete(path)
        .then(() => {
          this.getCandidates();
        })
        .catch((error) => {
          console.log(error);
          this.getCandidates();
        });
    },
    // Handles delete button
    deleteCandidate(candidate) {
      this.removeCandidate(candidate.id);
    },
    putCandidate(candidateID) {
      const path = `http://localhost:5000/candidates/${candidateID}`;
      axios
        .put(path)
        .then(() => {
          this.getCandidates();
          this.message = "Candidate Removed 🗑️";
          this.showMessage = false;
        })
        .catch((error) => {
          console.log(error);
          this.getCandidates();
        });
    },
    // Handles upvote button
    upvoteCandidate(candidate) {
      this.putCandidate(candidate.id);
    },
  },
  created() {
    this.getCandidates();
  },
};
</script>

<style scoped></style>
