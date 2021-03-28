import axios from 'axios'

const state = {
  form: {}
}

const getters = {}

const mutations = {
  setForm (state, form) {
    state.form = form
}

const actions = {

  getForm (context, formTitle) {
    return axios.get('http://127.0.0.1:8000/api/form/form_view?title=' + userId)
      .then(response => { context.commit('setForm', response.data) })
      .catch(e => { console.log(e) })
  },
  createForm (context, payload) {
    return axios.post('http://127.0.0.1:8000/api/form/form_create', payload)
  },
  deleteForm (context, formTitle) {
    return axios.delete('http://127.0.0.1:8000/api/form/form_delete?title=' + formTitle)
      .then(response => {})
      .catch(e => { console.log(e) })
  }

}

export default {
  state,
  getters,
  mutations,
  actions
}
