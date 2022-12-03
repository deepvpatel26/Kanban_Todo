<template>
    <div>
        <Navbar/>
  <div class="container mt-5">
    
    <h1>Title:</h1>
    <h2>{{article.title}}</h2>
    <h1>Data:</h1>
    <h2>{{article.listd}}</h2>
    <h1>published Date:</h1>
    <h2>{{article.date}}</h2>

    <router-link class="btn btn-warning mx-3 mt-3" :to="{name:'Listupdate', params:{id:article.id}}">Edit/Update</router-link>

    <button class="btn btn-danger mx-3 mt-3" @click="deleteData">Delete</button>  
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
            article:{}
        }
    },
    props:{
        id:{
            type:[Number,String],
            required:true,
        }
    },
    methods: {
        deleteData(){
            fetch(`http://localhost:5000/delete/${this.id}/`, {
                    method:"DELETE",
                    headers: {
                        "Content-Type":"application/json"
                    }
                })
                .then(() => {
                   this.$router.push({
                    name:'Home'
                   })
                })
                .catch(error => {
                    console.log(error)
                })
        },

        getdata(){
                fetch(`http://localhost:5000/get/${this.id}/`, {
                    method:"GET",
                    headers: {
                        "content-Type":"application/json"
                    }
                })
                .then(resp => resp.json())
                .then(data => {
                   this.article = data
                })
                .catch(error => {
                    console.log(error)
                });
            }
        },

        created() {
            this.getdata()
        }
}
</script>

<style>

</style>