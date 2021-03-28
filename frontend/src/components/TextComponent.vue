<template>
  <div class="form-group">
    <label for="{{ id }}">{{ name }}</label>
    <textarea id="{{ id }}" class="form-control" rows="4">{{ value }}</textarea>
  </div>
</template>

<script>
export default {
  name: 'TextComponent'
}
</script>

<style>
</style>
