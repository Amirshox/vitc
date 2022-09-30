<template>
  <div>
    <form name="form" @submit.prevent="handleRegister">
      <div v-if="!successful">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            v-model="user.username"
            v-validate="'required|min:3|max:20'"
            type="text"
            class="form-control"
            name="username"
          />
          <div v-if="submitted && errors.has('username')" class="alert-danger">
            {{ errors.first("username") }}
          </div>
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input
            v-model="user.password"
            v-validate="'required|min:6|max:40'"
            type="password"
            class="form-control"
            name="password"
          />
          <div v-if="submitted && errors.has('password')" class="alert-danger">
            {{ errors.first("password") }}
          </div>
        </div>
        <div class="form-group">
          <button class="btn btn-primary btn-block">Sign Up</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>