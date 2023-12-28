<template>
  <div class="login-container">
    <img src="../assets/login2.png" style="width: 100%;height: 100%"/>
    <div class="login_box">
      <!-- 头像区域 -->
      <div class="avatar_box">
        <img src="../assets/login.png"/>
      </div>
      <!-- 表单区域 -->
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
        <!-- 用户名区域 -->
        <el-form-item prop="username">
          <el-input type="text" v-model="loginForm.username" prefix-icon="el-icon-user" placeholder="请输入登录账号"></el-input>
        </el-form-item>
        <!-- 密码区域 -->
        <el-form-item prop="password">
          <el-input type="password" v-model="loginForm.password" prefix-icon="el-icon-lock" placeholder="请输入登录密码"></el-input>
        </el-form-item>
        <!-- 按钮区域区域 -->
        <el-form-item class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  axios.defaults.baseURL = 'http://8.141.9.251:8080';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://8.141.9.251:8081';
axios.defaults.headers.common['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE';
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Content-Type';
export default {
  name: 'Login',
  data () {
    return {
      // 这是登录表单的数据绑定对象
      loginForm: {
        username: '',
        password: ''
      },
      loginFormRules: {
        // 验证用户名是否合法
        username: [
          { required: true, message: '请输入登录用户名', trigger: 'blur' },
          { min: 5, max: 12, message: '长度在 5 到 12 个字符', trigger: 'blur' }
        ],
        // 验证密码是否合法
        password: [
          { required: true, message: '请输入登录密码', trigger: 'blur' },
          { min: 5, max: 12, message: '长度在 6 到 12 个字符', trigger: 'blur' }
        ]
      },
      student_passwd:{},
      valid_meg:false
    }
  },
  methods: {
    // 点击重置按钮重置表单
    resetLoginForm () {
      // 重置验证信息
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      if (this.loginForm.username==='Admin' && 
              this.loginForm.password==='123456') 
              {this.valid_meg=true
                sessionStorage.setItem('AdminName', this.loginForm.username)
                sessionStorage.setItem('AdminPassword', this.loginForm.password)
              // 路由的处理
              this.$router.push({
                  path: '/Home'
                })
              }
      this.$refs.loginFormRef.validate(valid => {
        axios({
                    url: 'http://8.141.9.251:8080/students/getstudentsById',
                    params: {
                        sid: this.loginForm.username }})
        .then(response => {
          if(!valid)  return
          let result = response.data
          if (result.student) {
            this.student_passwd = result.student
           
            if(this.loginForm.username=== this.student_passwd[0] && 
              this.loginForm.password===this.student_passwd[4]) 
              { this.valid_meg=true}
          if(this.valid_meg===true){
            sessionStorage.setItem('AdminName', this.loginForm.username)
            sessionStorage.setItem('AdminPassword', this.loginForm.password)
            // 路由的处理
            this.$router.push({
              path: '/Home'
            })
            // 使用消息提示登录成功，注意：消息组件在使用直接传，当然也可以设置其他的属性（对象的形式）
            return this.$message.success(result.msg)
            } 
          else {
            alert("登录失败")
            this.$router.push({
              path: '/login'
            })
            // 使用消息提示登录失败
            return this.$message.error(result.msg)
          }
          } else {
            this.$message.error('获取学生信息时出现错误!')
          }
        })
        .catch(error => {
          console.error('无该学生信息！', error);
        });

        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
  .login-container{
    background-color: #373D41;
    height: 100%;
  }
  .login_box{
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 3px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  .avatar_box{
    background-color: #fff;
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    img{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
  /*将按钮们放在右边*/
  .btns{
    display: flex;
    justify-content: flex-end;
  }
  .login_form{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    /*调整输入框的宽度*/
    box-sizing: border-box;
  }
</style>
