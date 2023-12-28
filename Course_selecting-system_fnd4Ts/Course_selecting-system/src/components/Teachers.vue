<template>
    <div>
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>教师管理</el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <!-- 卡片视图区域:搜索部分 -->
      <el-form v-model="getteachersQueryInfo">
        <el-row :gutter="20">
          <el-col :span="10">
            <el-form-item label="教师编号：">
              <el-input placeholder="请输入教师编号: " style="width: 400px" v-model="getteachersQueryInfo.query"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item style="margin-left: 100px">
              <el-button type="primary" icon="el-icon-search" @click="getteachersById(getteachersQueryInfo.query)">查询</el-button>
              <el-button type="danger" icon="el-icon-refresh" @click="getteachersNoLike">重置</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <el-dialog
      title="编辑学生信息"
      :visible.sync="queryteachersDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>学生教师管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑教师信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 教师信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="教师编号：">
              <el-input style="width: 800px" v-model="teachersById_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="教师姓名：">
              <el-input style="width: 800px" v-model="teachersById_query[1]"></el-input>
            </el-form-item>            
            <el-form-item label="邮箱：">
              <el-input style="width: 800px" v-model="teachersById_query[2]"></el-input>
            </el-form-item>            
            <el-form-item label="薪水：">
              <el-input style="width: 800px" v-model="teachersById_query[3]"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="queryteachersDialogVisible = false">关 闭</el-button>
        <el-button type="primary" @click="updateteachers()">提 交</el-button>
        <el-button type="danger"  @click="deleteteachersById(teachersById_query[0])">删除</el-button>
      </span>
    </el-dialog>

      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <!-- 卡片视图区域:列表部分 -->
      <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addteachersDialogVisible = true">新增教师信息</el-button>
      <el-table
        :data="teachersList"
        border
        style="width: 100%">
        <el-table-column
          prop="tid"
          label="教师编号"
          align="center"
          width="150px">
          <template slot-scope="teachersList">
          <p v-text="teachersList.row[0]"></p>
        </template>
        </el-table-column>
        <el-table-column
          prop="tname"
          label="教师名称"
          align="center">
          <template slot-scope="teachersList">
          <p v-text="teachersList.row[1]"></p>
        </template>
        </el-table-column>
        <el-table-column
          prop="email"
          label="邮箱"
          align="">
          <template slot-scope="teachersList">
          <p v-text="teachersList.row[2]"></p>
        </template>
        </el-table-column>
        <el-table-column
          prop="salary"
          label="薪水"
          align="center">
          <template slot-scope="teachersList">
          <p v-text="teachersList.row[3]"></p>
        </template>0 
        </el-table-column>
        <el-table-column
          label="操作"
          width="265px"
          align="center">
          <template slot-scope="teachersList">
            <el-button type="primary" icon="el-icon-view" size="mini" @click="getteachersById(teachersList.row[0])">编辑</el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleteteachersById(teachersList.row[0])">删除</el-button>
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
        title="新增教师信息"
        :visible.sync="addteachersDialogVisible"
        width="65%">
        <!-- 内容的主体区域 -->
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/home' }">
            <i class="el-icon-s-home"></i>首页
          </el-breadcrumb-item>
          <el-breadcrumb-item>教师信息管理</el-breadcrumb-item>
          <el-breadcrumb-item><b>新增教师</b></el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 设置分割线 -->
        <el-divider></el-divider>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <i class="el-icon-document"></i>
            <span> 教师信息</span>
          </div>
          <!-- 表单信息 -->
          <div style="margin-left: 3%">
            <el-form :model="addteachersForm">
              <el-form-item label="教师编号：" required="true">
                <el-input style="width: 800px" v-model="addteachersForm.tid"></el-input>
              </el-form-item>
              <el-form-item label="教师名称：" required="true">
                <el-input style="width: 800px" v-model="addteachersForm.tname"></el-input>
              </el-form-item>
              <el-form-item label="邮箱：">
                <el-input style="width: 800px" v-model="addteachersForm.email"></el-input>
              </el-form-item>
              <el-form-item label="薪水：">
                <el-input style="width: 800px" v-model="addteachersForm.salary"></el-input>
              </el-form-item>
              
            </el-form>
          </div>
        </el-card>
        <!-- 内容的底部区域 -->
        <span slot="footer" class="dialog-footer">
          <el-button @click="addteachersDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="addteachers()">提 交</el-button>
        </span>
      </el-dialog>
      <!-- 编辑新闻对话框 -->
      <el-dialog
        title="编辑教师信息"
        :visible.sync="updateteachersDialogVisible"
        width="65%">
        <!-- 内容的主体区域 -->
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/home' }">
            <i class="el-icon-s-home"></i>首页
          </el-breadcrumb-item>
          <el-breadcrumb-item>教师信息管理</el-breadcrumb-item>
          <el-breadcrumb-item><b>编辑教师信息</b></el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 设置分割线 -->
        <el-divider></el-divider>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <i class="el-icon-document"></i>
            <span> 教师信息</span>
          </div>
          <!-- 表单信息 -->
          <div style="margin-left: 3%">
            <el-form>
              <el-form-item label="教师编号：">
                <el-input style="width: 800px" v-model="teachersById[0]" disabled></el-input>
              </el-form-item>
              <el-form-item label="教师名称：">
                <el-input style="width: 800px" v-model="teachersById[1]" disabled></el-input>
              </el-form-item>
              <el-form-item label="邮箱：">
                <el-input style="width: 800px" v-model="teachersById[2]"></el-input>
              </el-form-item>
              <el-form-item label="薪水：">
                <el-input style="width: 800px" v-model="teachersById[3]"></el-input>
              </el-form-item>
              
            </el-form>
          </div>
        </el-card>
        <!-- 内容的底部区域 -->
        <span slot="footer" class="dialog-footer">
          <el-button @click="updateteachersDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="updateteachers()">提 交</el-button>
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
    name: 'teachers',
    data () {
      return {
        addteachersForm: {
          tid: '',
          tname:'',
          email: '',
          salary: ''
        },
        getteachersQueryInfo: {
          query: '',
          pageSize: 5,
          pageNum: 1
        },
        getteachersByIdInfo: {
          tid: ''
        },
        updateteachersInfo: {
          tid: '',
          email: '',
          salary: ''
        },
        deleteteachersByIdInfo: {
          tid: ''
        },
        teachersById: {},
        teachersById_query: {},
        total: 0,
        teachersList: [],
        // 控制添加对话框显示与隐藏
        addteachersDialogVisible: false,
        // 控制编辑对话框显示与隐藏
        updateteachersDialogVisible: false,
        // 控制查询对话框显示与隐藏
        queryteachersDialogVisible: false
      }
    },
    created () {
      this.getteachersList()
    },
    methods: {
      addteachers () {
        if (this.addteachersForm.tid !== '' && this.addteachersForm.tname !== '' && this.addteachersForm.email !== ''
        && this.addteachersForm.salary !== '') {
          // 发送请求重新修改密码
          const data = {
          tid:this.addteachersForm.tid,
          tname:this.addteachersForm.tname,
          email:this.addteachersForm.email,
          salary:this.addteachersForm.salary
        };
         // 发送POST请求
        axios.post('http://8.141.9.251:8080/addteachers', data)
          .then(response => {
            // 获取响应数据
            let result = response.data;
            if (result.message !== 'Teachers added successfully') {
              this.$message.error(result.message);
            } else {
              this.$router.push('/teachers');
              this.addteachersDialogVisible = false;
              this.getteachersList();
              this.$message.success(result.message);
            }
          })
          .catch(error => {
            console.error('添加老师时出错:', error);
            this.$message.error('添加老师失败');
          });
      } else {
        alert('输入有误，请重新输入！');
      }
      this.addteachersForm = Object.assign({}, this.initialValues)
    },
      getteachersList () {
        // 发送请求
        axios.get('http://8.141.9.251:8080/teachers')
          .then(response => {
            // 获取响应数据
            let result = response.data
            if (result.teachers.length ===0) {
              return this.$message.warning('获取教师列表失败!')
            } else {
              // 获取新闻列表成功
              this.pageNum = result.pageNum
              this.pageSize = result.pageSize
              this.teachersList = result.teachers
              this.total = result.totalCount
            }
          })
          .catch(error => {
        this.$message.error('获取老师列表失败!')
      })
      },
      getteachersById (tid) {
        this.getteachersByIdInfo.tid = tid
        // 发送请求
        axios({ url: 'http://8.141.9.251:8080/teachers/getteachersById',
                params: {tid: tid}
                })
                .then(response => {
          let result = response.data
          if (result.teacher) {
            this.updateteachersDialogVisible = true
            this.teachersById = result.teacher
          } else {
            this.$message.error('根据教师编号获取学生信息失败!')
          }
        })
        .catch(error => {
          console.error('获取教师信息时出现错误:', error);
        });
    },
    getteachersById_query (tid) {
        this.getteachersByIdInfo.tid = tid
        // 发送请求
        axios({ url: 'http://8.141.9.251:8080/teachers/getteachersById',
                params: {tid: tid}
                })
                .then(response => {
          let result = response.data
          if (result.teacher) {
            this.queryteachersDialogVisible = true
            this.teachersById_query = result.teacher
          } else {
            this.$message.error('根据教师编号获取学生信息失败!')
          }
        })
        .catch(error => {
          console.error('获取教师信息时出现错误:', error);
        });
    },
      deleteteachersById (tid) {
        this.deleteteachersByIdInfo.tid = tid
        if (confirm('确定要删除吗?')) {
          // 发送请求
          axios({ url: 'http://8.141.9.251:8080/teachers/deleteteachersById',
              params: { tid: tid }
                })
              .then(response => {
              // 获取响应数据
              let result = response.data
              console.log(result)
              if (result.message === 'Teacher deleted successfully') {
              this.getteachersByIdInfo.pageNum = 1
              this.getteachersList()
              this.$message.success('删除教师信息成功!')
              } else {
              this.$message.error('删除教师信息失败!')
              }
            }).catch(error => {
          console.error('删除教师信息失败:', error)
          this.$message.error('删除教师信息失败!')
          })
        }
      },
      updateteachers() {
        // 发送请求
        const data = {
        tid:this.teachersById[0],
        email: this.teachersById[2],
        salary: this.teachersById[3],
        };
        
        axios.post('http://8.141.9.251:8080/teachers/updateteachers', data)
          .then(response => {
            // 获取响应数据
            
            let result = response.data
            if (result.message !== 'teachers updated successfully') {
              return this.$message.error(result.msg)
            } else {
            this.$router.push('/teachers');
            this.updateteachersDialogVisible = false
            this.queryteachersDialogVisible = false
            this.getteachersList()
            this.$message.success(result.msg)
          }
        }).catch(error => {
          console.error('编辑教师信息时出现错误:', error);
        });
      },
      handleSizeChange (newSize) {
        this.getteachersQueryInfo.pageSize = newSize
        this.getteachersList()
      },
      handleCurrentChange (newSize) {
        this.getteachersQueryInfo.pageNum = newSize
        this.getteachersList()
      },
      getteachersByLike (newQuery) {
        this.query = newQuery
        this.getteachersList()
      },
      getteachersNoLike () {
        this.getteachersQueryInfo.query = ''
        this.getteachersList()
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
  