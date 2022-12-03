<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
      <a class="navbar-brand text-style" style="font-size: 50px;">Todo</a> 
        <!-- <router-link class="navbar-brand text-style" to="/">Home Page</router-link> -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item mx-2">
            <router-link class="btn btn-primary" aria-current="page" to="/home">Home</router-link>
          </li>
         
          <li class="nav-item">
            <router-link class="btn btn-success" to="/create">create</router-link>
          </li>
        </ul>
      </div>
    </div>
    </nav>
    </template>
    
    <script>
    export default {
    
    }
    </script>
    
    <style>
    .text-style{
      font-size: 50px ;
      font-family: 'Courier New', Courier, monospace;
      font-weight: bolder;
      color: brown;
    }
    </style>