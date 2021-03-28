<template>
  <div class="form-group">
    <label for="{{ id }}">{{ name }}</label>
    <input type="text" id="{{ id }}" value="{{ value }}" class="form-control">
  </div>
</template>

<script>
export default {
  name: 'StringComponent'
}
</script>

<style>
</style>
