<template>
  <div style="color: red;">tt proyecto vuxko, ema actual: {{ema}}
  <div>

  <label for="nombre">nombre</label>
  <input type="text" v-model="form.name" id="name" name="name">

  <label for="description">descripcion</label>
  <input type="text" v-model="form.description" id="description" name="description">

  <label for="activo">ufuuu a activo:</label>

  <select name="activo" v-model="form.estado" id="activo">
    <option value="activo">activo</option>
    <option value="desactivado">desactivado</option>
	</select>
  <select name="temp" v-model="form.temp" id="temp">
    <option value="15m">15m</option>
    <option value="1h">1h</option>
    <option value="4h">4h</option>
  </select>
  asdsd
  <div v-for="indi, key in form.indicadores" :key="key">
  <multi-indicator v-model:name="indi.name" v-model:parameters="indi.parameters" v-model:condition="indi.condition"></multi-indicator>
  </div>
  </div>
  <button @click="callEma">updateema</button>
  <button @click="agregar">add</button>
  <button @click="saveBot">post</button>
  <div v-for="bot in bots" :key="bot.id">
   <a :href="'seebot/'+bot.id">{{bot.id}} {{bot.temp}}</a> 
    <div v-for="indi in bot.indicators" :key="indi.id">
    {{indi.name}} {{indi.parameters}}{{indi.condition}}
    </div>
  </div>
  </div>
</template>

<script>
import MultiIndicator from './Indicator.vue'
import axios from 'axios'
export default {
  name: 'HelloDjango',
  data(){
    return {
    a:"asdas",
      ema: 0, 
      form: {
        name:"",
        description:"",
        estado:"activo",
        temp:"1h",
        indicadores: [{name:"ema",parameters:"20",condition:"menor"}]
      },
      bots: []
    }
  },
  mounted() {
    axios.get("/bot")
        .then( (response) => {this.bots = response.data.bots});
  },
  components: {
    MultiIndicator
  },
  methods: {
    call() {
      axios.get("/bot")
        .then(response => alert(response.data.ok));
    },
    callEma() {
      axios.get("/getema")
        .then(response =>{this.ema = response.data.ema});
    },
    saveBot() {
      axios.post("/botsave",this.form)
        .then(response => alert(response.data.ok));
    },
    agregar() {
      this.form.indicadores.push({name:"ema",parameters:"20",condition:"menor"})
    },
  }
}
</script>

<style scoped>

</style>