<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>学生管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:搜索部分 -->
    <el-form v-model="getstudentsQueryInfo">
      <el-row :gutter="20">
        <el-col :span="10">
          <el-form-item label="学生学号：">
            <el-input placeholder="请输入学生学号" style="width: 400px" v-model="getstudentsQueryInfo.query"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item style="margin-left: 100px">
            <el-button type="primary" icon="el-icon-search" @click="getstudentsById(getstudentsQueryInfo.query)">查询</el-button>
            <el-button type="primary" icon="el-icon-refresh" @click="getstudentsNoLike">重置</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog
      title="编辑学生信息"
      :visible.sync="querystudentsDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>学生信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑学生信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 学生信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="学生编号：">
              <el-input style="width: 800px" v-model="studentsById_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="学生名称：">
              <el-input style="width: 800px" v-model="studentsById_query[1]"></el-input>
            </el-form-item>
            <el-form-item label="邮箱：">
              <el-input style="width: 800px" v-model="studentsById_query[2]"></el-input>
            </el-form-item>
            <el-form-item label="年级：">
               <el-input style="width: 800px" v-model="studentsById_query[3]"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="querystudentsDialogVisible = false">取 消</el-button>
        <el-button type="primary"  @click="updatestudents()">提 交</el-button>
        <el-button type="danger"   @click="deletestudentsById(studentsById_query[0])">删除</el-button>
      </span>
    </el-dialog>

    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:列表部分 -->
    <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addstudentsDialogVisible = true">新增学生信息</el-button>
    <el-table
      :data="studentsList"
      border
      style="width: 100%">
      <el-table-column
        prop="sid"
        label="学生编号"
        align="center"
        width="150px">
        <template slot-scope="studentsList">
          <p v-text="studentsList.row[0]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="sname"
        label="学生名称"
        align="center">
        <template slot-scope="studentsList">
          <p v-text="studentsList.row[1]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="email"
        label="邮箱"
        align="center">
        <template slot-scope="studentsList">
          <p v-text="studentsList.row[2]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="grade"
        label="年级"
        align="center">
        <template slot-scope="studentsList">
          <p v-text="studentsList.row[3]"></p>
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        width="265px"
        align="center">
        <template slot-scope="studentsList">
          <el-button type="primary" icon="el-icon-view" size="mini" @click="getstudentsById(studentsList.row[0])">编辑</el-button>
          <el-button type="danger" icon="el-icon-delete" size="mini" @click="deletestudentsById(studentsList.row[0])">删除</el-button>
        </template>
      </el-table-column>
   
    </el-table>
    <!-- 分页区域 -->
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="pageNum"
        :page-sizes="[1, 2, 4, 5]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total">
      </el-pagination>
    </div>
    <!-- 添加新闻对话框 -->
    <el-dialog
      title="新增学生信息"
      :visible.sync="addstudentsDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>学生信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>新增学生</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 学生信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form :model="addstudentsForm">
            <el-form-item label="学生编号：" required="true">
              <el-input style="width: 800px" v-model="addstudentsForm.sid"></el-input>
            </el-form-item>
            <el-form-item label="学生名称：" required="true">
              <el-input style="width: 800px" v-model="addstudentsForm.sname"></el-input>
            </el-form-item>
            <el-form-item label="邮箱：" required="true">
              <el-input style="width: 800px" v-model="addstudentsForm.email"></el-input>
            </el-form-item>
            <el-form-item label="年级：">
              <el-input style="width: 800px" v-model="addstudentsForm.grade"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addstudentsDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addstudents()">提 交</el-button>
      </span>
    </el-dialog>
    <!-- 编辑新闻对话框 -->
    <el-dialog
      title="编辑学生信息"
      :visible.sync="updatestudentsDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>学生信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑学生信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 学生信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="学生编号：">
              <el-input style="width: 800px" v-model="studentsById[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="学生名称：">
              <el-input style="width: 800px" v-model="studentsById[1]" disabled></el-input>
            </el-form-item>
            <el-form-item label="邮箱：">
              <el-input style="width: 800px" v-model="studentsById[2]"></el-input>
            </el-form-item>
            <el-form-item label="年级：">
               <el-input style="width: 800px" v-model="studentsById[3]"></el-input>
            </el-form-item>
            <el-form-item label="密码更改：">
               <el-input style="width: 800px" v-model="studentsById[4]"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="updatestudentsDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="updatestudents()">提 交</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios';
axios.defaults.baseURL = 'http://8.141.9.251:8080';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://8.141.9.251:8081';
axios.defaults.headers.common['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE';
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Content-Type';
export default {
  name: 'students',
  data () {
    return {
      addstudentsForm: {
        sname: '',
        email: '',
        grade: '',
        sid:'',
        password:''
      },
      getstudentsQueryInfo: {
        query: '',
        pageSize: 5,
        pageNum: 1
      },
      getstudentsByIdInfo: {
        sid: ''
      },
      updatestudentsInfo: {
        sid: '',
        email: '',
        grade: '',
        password:''
      },
      deletestudentsByIdInfo: {
        sid: ''
      },
      studentsById: {},
      studentsById_query:{},
      total: 0,
      studentsList: [],
      // 控制添加对话框显示与隐藏
      addstudentsDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      updatestudentsDialogVisible: false,
      // 控制查询对话框显示与隐藏
      querystudentsDialogVisible:false
    }
  },
  created () {
    this.getstudentsList()
  },
  methods: {
      addstudents() {
      if (this.addstudentsForm.sid !== '' && this.addstudentsForm.sname !== '' && this.addstudentsForm.email !== '' 
      && this.addstudentsForm.grade !== ''  ) {
        // 构造要发送的数据
        const data = {
          sid:this.addstudentsForm.sid,
          sname:this.addstudentsForm.sname,
          email:this.addstudentsForm.email,
          grade:this.addstudentsForm.grade,
          password:123456
        };

        // 发送POST请求
        axios.post('http://8.141.9.251:8080/addstudents', data)
          .then(response => {
            // 获取响应数据
            let result = response.data;
            if (result.message !== 'Students added successfully') {
              this.$message.error(result.message);
            } else {
              this.$router.push('/students');
              this.addstudentsDialogVisible = false;
              this.getstudentsList();
              this.$message.success(result.message);
            }
          })
          .catch(error => {
            console.error('添加学生时出错:', error);
            this.$message.error('添加学生失败');
          });
      } else {
        alert('输入有误，请重新输入！');
      }
      this.addstudentsForm = Object.assign({}, this.initialValues)
    },
    getstudentsList () {
      // 发送请求
      axios.get('http://8.141.9.251:8080/students')
        .then(response => {
          // 获取响应数据
          let result = response.data
          if (result.students.length ===0) {
            return this.$message.warning('获取学生列表失败!')
          } else {
            // 获取新闻列表成功
            this.pageNum = result.pageNum
            this.pageSize = result.pageSize
            this.studentsList = result.students
            this.total = result.totalCount
          }
        })
        .catch(error => {
        this.$message.error('获取学生列表失败!')
    })
    },
      getstudentsById (sid) {
        axios({
                    url: 'http://8.141.9.251:8080/students/getstudentsById',
                    params: {
                        sid: sid
                    }
                })
        .then(response => {
          let result = response.data
          if (result.student) {
            this.updatestudentsDialogVisible = true
            this.studentsById = result.student
          } else {
            this.$message.error('根据学生编号获取学生信息失败!')
          }
        })
        .catch(error => {
          console.error('获取学生信息时出现错误:', error);
        });
    }
    ,
    getstudentsById_query(sid) {
        axios({
                    url: 'http://8.141.9.251:8080/students/getstudentsById',
                    params: {
                        sid: sid
                    }
                })
        .then(response => {
          let result = response.data
          if (result.student) {
            this.querystudentsDialogVisible = true
            this.studentsById_query = result.student
          } else {
            this.$message.error('根据学生编号获取学生信息失败!')
          }
        })
        .catch(error => {
          console.error('获取学生信息时出现错误:', error);
        });
    },
    deletestudentsById(sid) {
    if (confirm('确定要删除吗?')) {
      axios({
                    url: 'http://8.141.9.251:8080/students/deletestudentsById',
                    params: {
                        sid: sid
                    }
                })
      // axios.get(`http://localhost:8080/deletestudentsById/${sid}`)
        .then(response => {
          let result = response.data
          console.log(result)
          if (result.message === 'Student deleted successfully') {
            this.getstudentsByIdInfo.pageNum = 1
            this.getstudentsList()
            this.$message.success('删除学生信息成功!')
          } else {
            this.$message.error('删除学生信息失败!')
          }
        })
        .catch(error => {
          console.error('删除学生信息失败:', error)
          this.$message.error('删除学生信息失败!')
        })
    }
  },
    updatestudents () {

      const data = {
        sid:this.studentsById[0],
        email: this.studentsById[2],
        grade: this.studentsById[3],
        password :this.studentsById[4]
        };

      // 发送请求
      axios.post('http://8.141.9.251:8080/students/updatestudents', data)
        .then(response => {
          // 获取响应数据
          let result = response.data
        
          if (result.message !== 'students updated successfully') {
            return this.$message.error(result.msg)
          } else {
            this.$router.push('/students');
            this.updatestudentsDialogVisible = false
            this.querystudentsDialogVisible= false
            this.getstudentsList()
            this.$message.success(result.msg)
          }
        }) .catch(error => {
          console.error('编辑学生信息时出现错误:', error);
        });
    },
    handleSizeChange (newSize) {
      this.getstudentsQueryInfo.pageSize = newSize
      this.getstudentsList()
    },
    handleCurrentChange (newSize) {
      this.getstudentsQueryInfo.pageNum = newSize
      this.getstudentsList()
    },
    getstudentsByLike (newQuery) {
      this.query = newQuery
      this.getstudentsList()
    },
    getstudentsNoLike () {
      this.getstudentsQueryInfo.query = ''
      this.getstudentsList()
    }
  }
}
</script>

<style lang="less" scoped>
  /deep/.el-form-item__content {
    float: left;
  }
  .el-pagination{
    margin-top: 15px;
  }
  ul li{
    list-style: none;
    width: 400px;
    height: 40px;
    line-height: 40px;
  }
</style>
