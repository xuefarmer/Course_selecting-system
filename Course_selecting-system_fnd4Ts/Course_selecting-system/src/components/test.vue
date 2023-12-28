<template>
    <div>
      <button @click="getStudents">获取学生信息</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    methods: {
      getStudents() {
        axios.get('http://localhost:8080/students')
          .then(response => {
            console.log(response.data);
            this.students = response.data.students;
          })
          .catch(error => {
            console.error('获取学生信息时出错：', error);
          });
      }
    }
  };
  </script>
  