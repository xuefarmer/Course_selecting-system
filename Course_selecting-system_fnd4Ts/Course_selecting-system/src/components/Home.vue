<template>
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <img src="../assets/login.png" style="width: 65px;height: 65px;margin-left: 28px;margin-top: 0px" />
        <span style="margin-left: 30px">学生选课系统</span>
      </div>
      <div>
        <el-button type="info">
          <i class="el-icon-s-custom"></i>
          {{ adminName }}
        </el-button>
        <el-button type="info" @click="logout">
          <i class="el-icon-s-promotion"></i>
          退出
        </el-button>
      </div>
    </el-header>
    <!-- 主体区域 -->
    <el-container>
      <!-- 左侧边栏-->
      <el-aside width="200px">
        <el-menu background-color="#fff" text-color="#000" active-text-color="#409EFF" router default-active="/home">
          <el-menu-item index="/home">
            <i class="el-icon-s-home"></i>
            <span slot="title">首页</span>
          </el-menu-item>
          <!-- <el-menu-item index="/info">
            <i class="el-icon-help"></i>
            <span slot="title">查看个人信息</span>
          </el-menu-item>
          <el-menu-item index="/setPassword">
            <i class="el-icon-edit"></i>
            <span slot="title">修改登录密码</span>
          </el-menu-item> -->
          <el-menu-item v-if="adminName==='Admin'" index="/course">
            <i class="el-icon-notebook-2"></i>
            <span slot="title">课程管理</span>
          </el-menu-item>
          <el-menu-item index="/students">
            <i class="el-icon-user"></i>
            <span slot="title">学生信息管理</span>
          </el-menu-item>
          <el-menu-item index="/choices">
            <i class="el-icon-files"></i>
            <span slot="title">选课管理</span>
          </el-menu-item>
          <el-menu-item v-if="adminName==='Admin'" index="/teachers">
            <i class="el-icon-user-solid"></i>
            <span slot="title">教师管理</span>
          </el-menu-item>


          
        </el-menu>
      </el-aside>
      <!-- 右侧内容主体区域 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        adminName: sessionStorage.getItem('AdminName'),

        queryInfo: {
        aname: sessionStorage.getItem('AdminName'),
        apass: sessionStorage.getItem('AdminPassword')
      },
      }
    },
    methods: {
      logout() {
        window.sessionStorage.clear()
        this.$router.push('/login')
      }
    }
  }
</script>

<!-- 路由占位符 -->
<style lang="less" scoped>
  .home-container {
    height: 100%;
  }

  .el-header {
    background-color: #0665d0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #fff;
    padding-left: 0;
    font-size: 20px;
    font-family: "微软雅黑";

    >div {
      display: flex;
      align-items: center;

      span {
        margin-left: 15px;
      }
    }

    img {
      width: 100px;
      height: 100px;
    }
  }

  .el-aside {
    background-color: #e1effe;
    font-family: "微软雅黑";
      display: inline-block;
      padding: .5rem .625rem;
      margin: 2px 0;
  }

  .el-main {
    background-color: #eaedf1;
  }

  .el-button {
    color: #1c242c;
    background-color: #f2f6fc;
    border: none;
    font-size: 14px;

    &:hover {
      color: #2483ff;
      background-color: rgb(242, 246, 252);
    }

    &:active {
      color: #2483ff;
      background-color: rgb(242, 246, 252);
    }
  }
</style>
