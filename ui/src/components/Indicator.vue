<template>
  <div>
  <label for="indicador">Chossose a indicador:</label>
  <select name="indicador" id="indicador" :value="name" @change="$emit('update:name', $event.target.value)" >
    <option value="ema">ema</option>
    <option value="adx">adx</option>
  </select>
  <label for="valor">valor</label>
  <input type="text" :value="parameters" @input="$emit('update:parameters', $event.target.value)" id="valor" name="valor">
  <label for="condicion">condicion</label>
  <input type="text" :value="condition" @input="$emit('update:condition', $event.target.value)"  id="condicion" name="condicion">

  </div>
</template>

<script>
import axios from 'axios'
export default {
  props: {
      name: {
        type: String,
        required: true
      },
      parameters: {
        type: String,
        required: true
      },
      condition: {
        type: String,
        required: true
      }
    },
  name: 'MultiIndicator',
  methods: {
    call() {
      axios.get("/bot")
        .then(response => alert(response.data.ok));
    },
    saveBot() {
      axios.post("/botsave",{datos:23})
        .then(response => alert(response.data.ok));
    },
  }
}
</script>

<style scoped>

</style>