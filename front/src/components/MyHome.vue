<template>
    <div><Navbar/>
    <div class="container mt-5">
        <div v-for="article in articles" :key="article.id">
            <h3>
                <router-link class="link-style" 
                :to="{name:'Listarticle',params:{id:article.id}}">{{ article.title}}</router-link>
            </h3>
            <hr>
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
                articles:[],
            }
        },

        methods:{
            getArticles(){
                fetch('http://localhost:5000/', {
                    methods:"GET",
                    headers: {
                        "Content-Type":"application/json"
                    }
                })
                .then(resp => resp.json())
                .then(data => {
                   this.articles.push(...data)
                })
                .catch(error => {
                    console.log(error)
                })
            }
        },

        created() {
            this.getArticles()
        }
    }
    </script>
    
<style>
.link-style{
    font-weight: bold;
    color:black;
    text-decoration: none;
}
.link-style:hover{
    color:gray;
    text-decoration: none;
}

</style>