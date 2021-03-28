<template>
<div class="container">
  <div class="row my-5 py-3">
    <label>Form Title</label>
    <input type="text" name="form_title" id="form_title" class="form-control" v-model="form_title" placeholder="Form title" required>
    <div>
      <button type="submit" class="btn btn-lg btn-primary btn-block"  @click="doCreate">Create Form</button>
    </div>
    <div>
      <button type="submit" class="btn btn-lg btn-secondary btn-block"  @click="doView">View Form</button>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      form_title: ''
    }
  },
  methods: {
    doRegister () {

      this.$store.dispatch('postRegister', { title: this.form_title })
        .then(response => {
          this.$router.push('/')
        })
    }
  }
}
</script>

<style>
</style>
