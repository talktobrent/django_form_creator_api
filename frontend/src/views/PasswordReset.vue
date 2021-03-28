<template>
    <div class="container">
        <div class="row my-5 py-3">
            <div class="col-lg-8 offset-2">
                <div v-if="!passwordResetSubmitted" class="form-signin">
                    <div class="form-group">
                            <input type="email" id="inputEmail" class="form-control" placeholder="Email address" v-model="email" required autofocus>
                    </div>
                    <div class="checkbox mb-3">
                        <label>
                            <input type="checkbox" value="remember-me"> Remember me
                        </label>
                    </div>
                    <span class="btn btn-lg btn-primary btn-block"  @click="submitPasswordReset">Request Password Reset</span>
                </div>
                <div v-else class="text-center">
                    <h1>Password Reset Submitted</h1>
                    <p>You will receive an email momentarily to complete your password reset.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'PasswordReset',
  data () {
    return {
      email: '',
      passwordResetSubmitted: false
    }
  },
  methods: {
    submitPasswordReset () {
      this.$store.dispatch('postPasswordReset', { email: this.email })
        .then(response => {
          this.passwordResetSubmitted = true
        })
    }
  }
}
</script>

<style>
</style>
