<template>
  <div class="container mt-5">
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex justify-content-start">
        <div>
          <label for="">Search: </label>
          <input
            class="form-input form-control"
            v-model="filter.search"
            @input="setFilter"
          />
        </div>
        <div class="ml-4">
          <label for="">Tags: </label>
          <v-select
            :options="GET_TAGS"
            v-model="filter.tags"
            @input="setFilter"
            class="v__select "
            label="title"
            :reduce="item => item.id"
            multiple
          />
        </div>
      </div>
      <button
        class="btn btn-primary"
        @click="$router.push('/home/add-contact')"
      >
        Add
      </button>
    </div>
    <table class="table mt-2">
      <thead>
        <tr>
          <th>ID</th>
          <th>FullName</th>
          <th>Email</th>
          <th>Gender</th>
          <th>Telephone</th>
          <th>Father</th>
          <th>Mother</th>
          <th>Tags</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="user in GET_CONTACTS" :key="user.id">
          <td>
            {{ user.id }}
          </td>
          <td>
            {{ user.full_name }}
          </td>
          <td>
            {{ user.email }}
          </td>
          <td>
            {{ user.gender }}
          </td>
          <td>
            {{ user.phone_number }}
          </td>
          <td>
            <span v-if="user.father && user.father.full_name">
              {{ user.father.full_name }}
            </span>
          </td>
          <td>
            <span v-if="user.mother && user.mother.full_name">
              {{ user.mother.full_name }}
            </span>
          </td>
          <td>
            <div v-for="tag in user.tags" :key="tag.id">
              <span class="badge bg-success">
                {{ tag.title }}
              </span>
            </div>
          </td>
          <td>
            <div class="d-flex justify-content-start align-items-center">
              <button
                class="btn btn-warning btn-sm m-1"
                @click="$router.push(`/home/edit-contact/${user.id}`)"
              >
                Edit
              </button>
              <button
                class="btn btn-danger btn-sm"
                @click="deleteContact(user.id)"
              >
                Delete
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Home",

  data() {
    return {
      initTimeout: null,
      filter: {
        search: "",
        tags: []
      }
    };
  },

  computed: {
    ...mapGetters("contact", ["GET_CONTACTS", "GET_TAGS"])
  },

  methods: {
    ...mapActions("contact", [
      "FETCH_CONTACTS",
      "FETCH_TAGS",
      "DELETE_CONTACT"
    ]),

    async deleteContact(id) {
      await this.DELETE_CONTACT(id);
      this.FETCH_CONTACTS();
    },

    setFilter() {
      let query = new URLSearchParams();
      query.append("search", this.filter.search);
      // query.append("tags", this.filter.tags);
      for (let key of this.filter.tags) {
        query.append("tags", key);
      }
      console.log("query", query);

      clearTimeout(this.initTimeout);
      this.initTimeout = setTimeout(() => {
        this.FETCH_CONTACTS(query);
      }, 200);
    }
  },
  mounted() {
    this.FETCH_CONTACTS();
    this.FETCH_TAGS();
  }
};
</script>


<style scoped>
.v__select {
  cursor: text;
  width: 200px;
}
</style>