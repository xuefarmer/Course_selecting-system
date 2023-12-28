<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>课程管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:搜索部分 -->
    <el-form v-model="getCourseQueryInfo">
      <el-row :gutter="20">
        <el-col :span="10">
          <el-form-item label="课程编号：">
            <el-input placeholder="请输入课程编号" style="wcidth: 400px" v-model="getCourseQueryInfo.query"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item style="margin-left: 100px">
            <el-button type="primary" icon="el-icon-search" @click="getCourseBycid(getCourseQueryInfo.query)">查询</el-button>
            <el-button type="danger" icon="el-icon-refresh" @click="getCourseNoLike">重置</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog
      title="编辑学生信息"
      :visible.sync="queryCourseDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>课程信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑课程信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 课程信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="课程编号：">
              <el-input style="width: 800px" v-model="CourseBycid_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="课程名称：">
              <el-input style="width: 800px" v-model="CourseBycid_query[1]"></el-input>
            </el-form-item>            
            <el-form-item label="学时：">
              <el-input style="width: 800px" v-model="CourseBycid_query[2]"></el-input>
            </el-form-item>            
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="queryCourseDialogVisible = false">关 闭</el-button>
        <el-button type="primary" @click="updatestudents()">提 交</el-button>
        <el-button type="danger"  @click="deleteCourseBycid(CourseBycid_query[0])">删除</el-button>
      </span>
    </el-dialog>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:列表部分 -->
    <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addCourseDialogVisible = true">新增课程信息</el-button>
    <el-table
      :data="coursesList"
      border
      style="wcidth: 100%">
      <el-table-column
        prop="cid"
        label="课程编号"
        align="center"
        wcidth="150px">
        <template slot-scope="coursesList">
          <p v-text="coursesList.row[0]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="cname"
        label="课程名称"
        align="center">
        <template slot-scope="coursesList">
          <p v-text="coursesList.row[1]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="hour"
        label="学时"
        align="center">
        <template slot-scope="coursesList">
          <p v-text="coursesList.row[2]"></p>
        </template>
      </el-table-column>
      
      <!-- <el-table-column
        prop="tid"
        label="授课教师编号"
        align="center">
      </el-table-column> -->
      
      <el-table-column
        label="操作"
        wcidth="265px"
        align="center">
        <template slot-scope="coursesList">
          <el-button type="primary" icon="el-icon-view" size="mini" @click="getCourseBycid(coursesList.row[0])">编辑</el-button>
          <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleteCourseBycid(coursesList.row[0])">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 分页区域 -->
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="pageNum"
        :page-sizes="[1, 2, 3, 4, 5]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total">
      </el-pagination>
    </div>
    <!-- 添加新闻对话框 -->
    <el-dialog
      title="新增课程信息"
      :visible.sync="addCourseDialogVisible"
      wcidth="31%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>课程信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>新增课程</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divcider></el-divcider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 课程信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form :model="addCourseForm">
            <el-form-item label="课程编号：" required="true">
              <el-input style="wcidth: 400px" v-model="addCourseForm.cid"></el-input>
            </el-form-item>
            <el-form-item label="课程名称：" required="true">
              <el-input style="wcidth: 400px" v-model="addCourseForm.cname"></el-input>
            </el-form-item>
            <el-form-item label="学时：" required="true">
              <el-input style="wcidth: 400px" v-model="addCourseForm.hour"></el-input>
            </el-form-item>
            <!-- <el-form-item label="授课教师编号：" required="true">
              <el-input style="wcidth: 400px" v-model="addCourseForm.tid"></el-input>
            </el-form-item> -->

          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addCourseDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addCourse()">提 交</el-button>
      </span>
    </el-dialog>
    <!-- 编辑新闻对话框 -->
    <el-dialog
      title="编辑课程信息"
      :visible.sync="updateCourseDialogVisible"
      wcidth="31%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>课程信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑课程信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divcider></el-divcider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 课程信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="课程编号：">
              <el-input style="wcidth: 400px" v-model="CourseBycid[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="课程名称：">
              <el-input style="wcidth: 400px" v-model="CourseBycid[1]"></el-input>
            </el-form-item>
            <el-form-item label="学时：">
              <el-input style="wcidth: 400px" v-model="CourseBycid[2]"></el-input>
            </el-form-item>
            <!-- <el-form-item label="授课教师编号：">
              <el-input style="wcidth: 400px" v-model="CourseBycid.tid"></el-input>
            </el-form-item> -->
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="updateCourseDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateCourse()">提 交</el-button>
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
  name: 'Course',
  data () {
    return {
      addCourseForm: {
        cid: '',
        cname: '',
        hour: '',
      },
      getCourseQueryInfo: {
        query: '',
        pageSize: 5,
        pageNum: 1
      },
      getCourseBycidInfo: {
        cid: ''
      },
      updateCourseInfo: {
        cid: '',
        cname: '',
        hour: '',
      },
      deleteCourseBycidInfo: {
        cid: ''
      },
      CourseBycid: {},
      CourseBycid_query: {},
      total: 0,
      coursesList: [],
      // 控制添加对话框显示与隐藏
      addCourseDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      updateCourseDialogVisible: false,
      // 控制查询对话框显示与隐藏
      queryCourseDialogVisible: false
    }
  },
  created () {
    this.getCourseList()
  },
  methods: {
    addCourse() {
      if (this.addCourseForm.cname !== '' && this.addCourseForm.hour !== '' && this.addCourseForm.cid !== '') {
        // 发送请求重新修改密码
        const data = {
          cid:this.addCourseForm.cid,
          cname:this.addCourseForm.cname,
          hour:this.addCourseForm.hour,
        };
        // 发送POST请求
        axios.post('http://8.141.9.251:8080/addcourses', data)
          .then(response => {
            // 获取响应数据
            let result = response.data;
            if (result.message !== 'Courses added successfully') {
              this.$message.error(result.message);
            } else {
              this.$router.push('/course');
              this.addCourseDialogVisible = false;
              this.getCourseList();
              this.$message.success(result.message);
            }
          })
          .catch(error => {
            console.error('添加课程时出错:', error);
            this.$message.error('添加课程失败');
          });
      } else {
        alert('输入有误，请重新输入！');
      }
      this.addCourseForm = Object.assign({}, this.initialValues)
    },
    getCourseList() {
            // 发送请求
            axios.get('http://8.141.9.251:8080/courses')
        .then(response => {
          // 获取响应数据
          let result = response.data
          if (result.courses.length ===0) {
            return this.$message.warning('获取课程列表失败!')
          } else {
            // 获取新闻列表成功
            this.pageNum = result.pageNum
            this.pageSize = result.pageSize
            this.coursesList = result.courses
            this.total = result.totalCount
          }
        })
        .catch(error => {
        this.$message.error('获取课程列表失败!')
    })
    },
    getCourseBycid (cid) {
      // 发送请求
      axios({url: 'http://8.141.9.251:8080/courses/getcoursesById',
                    params: {
                        cid: cid
                    }
                })
                .then(response => {
          let result = response.data
          if (result.course) {
            this.updateCourseDialogVisible = true
            this.CourseBycid = result.course
          } else {
            this.$message.error('根据课程编号获取学生信息失败!')
          }
        })
        .catch(error => {
          console.error('获取课程信息时出现错误:', error);
        });
    },
    getCourseBycid_query (cid) {
      // 发送请求
      axios({url: 'http://8.141.9.251:8080/courses/getcoursesById',
                    params: {
                        cid: cid
                    }
                })
                .then(response => {
          let result = response.data
          if (result.course) {
            this.queryCourseDialogVisible = true
            this.CourseBycid_query = result.course
          } else {
            this.$message.error('根据课程编号获取学生信息失败!')
          }
        })
        .catch(error => {
          console.error('获取课程信息时出现错误:', error);
        });
    },
    deleteCourseBycid (cid) {
      if (confirm('确定要删除吗?')) {
      axios({
                    url: 'http://8.141.9.251:8080/courses/deletecoursesById',
                    params: {
                        cid: cid
                    }
                })
        .then(response => {
          let result = response.data
          console.log(result)
          if (result.message === 'Course deleted successfully') {
            this.getCourseBycidInfo.pageNum = 1
            this.getCourseList()
            this.$message.success('删除课程信息成功!')
          } else {
            this.$message.error('删除课程信息失败!')
          }
        })
        .catch(error => {
          console.error('删除课程信息失败:', error)
          this.$message.error('删除课程信息失败!')
        })
    }
  },
    updateCourse () {
    //   this.updateCourseInfo[0] = this.CourseBycid[0]
    //   this.updateCourseInfo.cname = this.CourseBycid.cname
    //   this.updateCourseInfo.hour = this.CourseBycid.hour
      const data = {
        cid:this.CourseBycid[0],
        cname: this.CourseBycid[1],
        hour: this.CourseBycid[2]
        };
      // 发送请求
      axios.post('http://8.141.9.251:8080/courses/updatecourses', data)
        .then(response => {
          // 获取响应数据
          let result = response.data
        
          if (result.message !== 'courses updated successfully') {
            return this.$message.error(result.msg)
          } else {
            this.$router.push('/course');
            this.updateCourseDialogVisible = false
            this.queryChoicesDialogVisible = false
            this.getCourseList()
            this.$message.success(result.msg)
          }
        }) .catch(error => {
          console.error('编辑课程信息时出现错误:', error);
        });
    },
    handleSizeChange (newSize) {
      this.getCourseQueryInfo.pageSize = newSize
      this.getCourseList()
    },
    handleCurrentChange (newSize) {
      this.getCourseQueryInfo.pageNum = newSize
      this.getCourseList()
    },
    getCourseByLike (newQuery) {
      this.query = newQuery
      this.getCourseList()
    },
    getCourseNoLike () {
      this.getCourseQueryInfo.query = ''
      this.getCourseList()
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
