<template>
  <div class="form-group">
    <label for="{{ id }}">{{ name }}</label>
    <input type="number" id="{{ id }}" value="{{ value }}" class="form-control">
  </div>
</template>

<script>
export default {
  name: 'IntComponent'
}
</script>

<style>
</style>
