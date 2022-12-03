import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/MyHome.vue'
import Create from './components/MyCreate.vue'
import Listarticle from './components/ListDetails.vue'
import Listupdate from './components/ListUpdate.vue'
import Login from './components/MyLogin.vue'

const routes = [
    { path:'/',
    name:'Login',
    component:Login },

    { path:'/home',
    name:'Home',
    component:Home },

    { path:'/create',
    name:'Create',
    component:Create },

    { path:'/listarticle/:id',
    name:'Listarticle',
    component:Listarticle,
    props:true},

    { path:'/listupdate/:id',
    name:'Listupdate',
    component:Listupdate,
    props:true},
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;