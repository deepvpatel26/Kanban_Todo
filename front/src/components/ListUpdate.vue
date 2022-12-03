<template>
    <div>
    <Navbar/>
  <div class="container mt-4">
    
    <form @submit.prevent="updatedata">
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
        Update Data
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

    props:{
        id:{
            type:[Number,String],
            required:true,
        }
    },
    data() {
    return {
      title:null,
      listd:null,
      error:null,
    }
  },
  methods:{
    updatedata(){
        fetch(`http://localhost:5000/update/${this.id}/`, 
                {
                    method:"PUT",
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
  },

  beforeRouteEnter(to,from,next){
    if(to.params.id != undefined) {
        fetch(`http://localhost:5000/get/${to.params.id}/`, {
                    methods:"GET",
                    headers: {
                        "Content-Type":"application/json"
                    }
                })
                .then(resp => resp.json())
                .then(data => {
                   return next(vm=>(vm.title=data.title, vm.listd=data.listd))
                })
                .catch(error => {
                    console.log(error)
                }) 
        } else {
            return next()
        }
  }

}
</script>

<style>

</style>