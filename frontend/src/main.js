import Vue from 'vue'
import store from '@/store/index.js'
import router from '@/router/index.js'

import axios from 'axios'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL

Vue.config.productionTip = false

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
