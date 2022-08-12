import { createApp } from 'vue'
import HelloDjango from './components/HelloDjango'
import SeeBot from './components/SeeBot'
import BaseLogin from './components/BaseLogin'
// Creamos una instancia de la aplicación Vue
const app = createApp({
  // Elemento html donde se va ha renderizar el contenido
  el: '#app',
  // Activamos el componente dentro de la app
  components : {
    HelloDjango,
    SeeBot,
    BaseLogin
  },
  // Creamos variable msg reactiva con ref
  data () {
    return {
      msg: 'Componente de VueJsasdasdadS 3'
    }
  },
})
// Montamos la app en el div #app de nuestra plantilla index.html.
app.mount('#app')
