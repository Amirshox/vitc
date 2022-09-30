<template>
  <div class="form-group-contact mt-5">
    <h3 v-if="this.$route.params.id">Edit Contact</h3>
    <h3 v-else>Add Contact</h3>

    <form name="form" @submit.prevent="onSubmit">
      <div>
        <div class="form-group">
          <label for="fullname">Full Name</label>
          <input
              v-model="contactData.full_name"
              type="text"
              class="form-control"
              name="full name"
          />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input
              v-model="contactData.email"
              type="email"
              class="form-control"
              name="email"
          />
        </div>

        <div class="form-group">
          <label for="phone_number">Phone Number</label>
          <input
              v-model="contactData.phone_number"
              placeholder="998 XX XXX XX XX"
              type="number"
              class="form-control"
              name="phone_number"
          />
        </div>

        <div class="form-group">
          <label for="">Gender: </label>
          <v-select
              v-model="contactData.gender"
              :options="genderOptions"
              class="v__select "
              label="title"
              :reduce="item => item.value"
          />
        </div>
        <div class="form-group">
          <label for="">Father: </label>
          <v-select
              v-model="contactData.father"
              :options="getFathers"
              class="v__select "
              label="full_name"
              :reduce="item => item.id"
          />
        </div>

        <div class="form-group">
          <label for="">Mother: </label>

          <v-select
              v-model="contactData.mother"
              :options="getMothers"
              class="v__select "
              label="full_name"
              :reduce="item => item.id"
          />
        </div>

        <!-- <pre>
          
          {{ GET_CONTACTS }}
        </pre> -->

        <div class="form-group">
          <label for="">Tags: </label>

          <v-select
              :options="GET_TAGS"
              class="v__select "
              v-model="contactData.tags"
              label="title"
              :reduce="item => item.id"
              multiple
          />
        </div>

        <div class="form-group">
          <button class="btn btn-primary btn-block">
            {{ this.$route.params.id ? "Edit Contact" : "Add Contact" }}
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  data() {
    return {
      contactData: {
        full_name: "",
        email: "",
        gender: "",
        phone_number: "",
        father: null,
        mother: null,
        tags: []
      },
      genderOptions: [
        {
          title: "MALE",
          value: "male"
        },
        {
          title: "FEMALE",
          value: "female"
        }
      ]
    };
  },

  computed: {
    ...mapGetters("contact", ["GET_CONTACTS", "GET_TAGS", "GET_ONE_CONTACT"]),

    getFathers() {
      if (this.$route.params.id) {
        const routerId = this.$route.params.id;
        return this.GET_CONTACTS.filter(
            item => item.id != routerId && item.gender == "male"
        );
      } else return this.GET_CONTACTS.filter(item => item.gender == "male");
    },
    getMothers() {
      // return this.GET_CONTACTS.filter(item => item.gender === "female");

      if (this.$route.params.id) {
        const routerId = this.$route.params.id;
        return this.GET_CONTACTS.filter(
            item => item.id != routerId && item.gender == "female"
        );
      } else return this.GET_CONTACTS.filter(item => item.gender == "female");
    }
  },

  methods: {
    ...mapActions("contact", [
      "FETCH_CONTACTS",
      "FETCH_TAGS",
      "FETCH_ONE_CONTACT",
      "UPDATE_CONTACT",
      "CREATE_CONTACT"
    ]),

    async onSubmit() {
      if (this.$route.params.id) {
        await this.UPDATE_CONTACT({
          id: this.$route.params.id,
          data: this.contactData
        });
      } else {
        await this.CREATE_CONTACT(this.contactData);
      }

      this.$router.push("/home");
    }
  },
  async mounted() {
    this.FETCH_CONTACTS();
    this.FETCH_TAGS();

    if (this.$route.params.id) {
      await this.FETCH_ONE_CONTACT(this.$route.params.id);
      const {
        email,
        full_name,
        mother,
        father,
        tags,
        gender,
        phone_number
      } = this.GET_ONE_CONTACT;

      this.contactData.email = email;
      this.contactData.full_name = full_name;
      this.contactData.mother = mother;
      this.contactData.father = father;
      for (let key of tags) {
        this.contactData.tags.push(key.id);
        // console.log('ket', key)
      }

      // this.contactData.tags = tags;
      this.contactData.phone_number = phone_number;
      this.contactData.gender = gender;
    }
  }
};
</script>

<style scoped>
.v__select {
  cursor: text;
  width: 100%;
}

.form-group-contact {
  width: 400px;
  margin: 0 auto;
}
</style>
