<template>
  <div>
    <Navbar/>
  <div class="container mt-4">
    <form @submit.prevent="insertData">
      <input 
      type="text" 
      class="form-control" 
      placeholder="Please enter your list name" 
      v-model="title"
      />
      <br/>

      <textarea 
      class="form-control" 
      placeholder="Please enter your note here"
      rows="10" v-model="listd">
      </textarea>
    
      <button class="btn btn-success mt-4">
        Publish Data
      </button>
      
    </form>

      <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5"
      role="alert">
        <strong>{{error}}</strong>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './MyNavbar.vue'

export default {
  name: 'App',
components: {
  Navbar
},
  data() {
    return {
      title:null,
      listd:null,
      error:null,
    }
  },
  methods: {
    insertData() {
      if(!this.title || !this.listd) {
        this.error = "Please add all the fields"
      } else {
        fetch('http://localhost:5000/add', 
                {
                    method:"POST",
                    headers: {"Content-Type":"application/json"
                            },
                    body: JSON.stringify({title:this.title, listd:this.listd})
                }
              )
                .then(resp => resp.json(),
                console.log(this.title,this.listd))
                .then(() => {
                   this.$router.push({
                    name:'Home'
                   })
                   
                })
                .catch(error => {
                    console.log(error)
                })
      }
    }
  },
}
</script>

<style>

</style>