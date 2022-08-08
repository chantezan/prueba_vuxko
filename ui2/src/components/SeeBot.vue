<template>
  <div style="color: red;">Inicio proyecto vuxko, ema actual: {{ema}}
  <div>
  <label for="activo">ufuuu a activo:</label>
  <label for="nombre">nombre</label>
  <input type="text" :value="form.name" id="name" name="name">
  <label for="description">descripcion</label>
  <input type="text" :value="form.description" id="description" name="description">
  <label for="activo">id bot {{id}}</label>

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
  <button @click="callEma">checkentrada</button>
  <button @click="agregar">add</button>
  <button @click="saveBot">post</button>
  <div>
    aka
    {{data_entrada.exito}}
    <div v-for="ema,key in data_entrada.emas" :key="key">
      {{ema}}
    </div>
  </div>
  </div>
</template>

<script>
import MultiIndicator from './Indicator.vue'
import axios from 'axios'
export default {
  props: ["id"],
  name: 'SeeBot',
  data(){
    return {
      ema: 0, 
      form: {
        name:"",
        description:"",
        estado:"activo",
        temp:"1h",
        indicadores: []
      },
      bots: [],
      data_entrada:{exito:false,emas:[]}
    }
  },
  mounted() {
    axios.get("/getonebot/"+this.id)
        .then( (response) => {this.form = response.data.bot});
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
      axios.get("/checkentrada/"+this.id)
        .then(response =>{this.data_entrada = response.data});
    },
    saveBot() {
      axios.post("/botsave/"+this.id,this.form)
        .then(response => alert(response.data.ok));
    },
    agregar() {
      this.form.indicadores.push({name:"ema",value:"20",condition:"menor"})
    },
  }
}
</script>

<style scoped>

</style>