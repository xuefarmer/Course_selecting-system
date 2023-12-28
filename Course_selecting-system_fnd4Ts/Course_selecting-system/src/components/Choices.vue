<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        <i class="el-icon-s-home"></i>首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>选课信息管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:搜索部分 -->
    <el-form v-model="getChoicesQueryInfo">
      <el-row :gutter="20">
        <el-col :span="10">
          <el-form-item label="课程编号：">
            <el-input placeholder="请输入课程编号" style="width: 400px" v-model="getChoicesQueryInfo.query"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item style="margin-left: 100px">
            <el-button type="primary" icon="el-icon-search" @click="getChoicesById(getChoicesQueryInfo.query)">查询</el-button>
            <el-button type="danger"  icon="el-icon-refresh" @click="getChoicesNoLike" >重置</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <el-dialog
      title="编辑学生信息"
      :visible.sync="queryChoicesDialogVisible"
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
            <el-form-item label="选课编号：">
              <el-input style="width: 800px" v-model="ChoicesById_query[0]" disabled></el-input>
            </el-form-item>
            <el-form-item label="学生编号：">
              <el-input style="width: 800px" v-model="ChoicesById_query[1]"></el-input>
            </el-form-item>            
            <el-form-item label="教师编号：">
              <el-input style="width: 800px" v-model="ChoicesById_query[2]"></el-input>
            </el-form-item>            
            <el-form-item label="课程编号">
              <el-input style="width: 800px" v-model="ChoicesById_query[3]"></el-input>
            </el-form-item>
            <el-form-item label="成绩">
              <el-input style="width: 800px" v-model="ChoicesById_query[4]"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="queryChoicesDialogVisible = false">关 闭</el-button>
        <el-button type="primary" @click="updatestudents()">提 交</el-button>
        <el-button type="danger"  @click="deleteChoicesById(ChoicesById_query[0])">删除</el-button>
      </span>
    </el-dialog>
    <!-- 设置分割线 -->
    <el-divider></el-divider>
    <!-- 卡片视图区域:列表部分 -->
    <el-button type="primary" icon="el-icon-plus" style="margin-bottom: 15px" @click="addChoicesDialogVisible = true">新增选课信息</el-button>
    <el-table
      :data="choicesList"
      border
      style="width: 100%">
      <el-table-column
        prop="no"
        label="选课编号"
        align="center"
        width="150px">
        <template slot-scope="choicesList">
          <p v-text="choicesList.row[0]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="sid"
        label="学生编号"
        align="center">
        <template slot-scope="choicesList">
          <p v-text="choicesList.row[1]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="tid"
        label="教师编号"
        align="center">
        <template slot-scope="choicesList">
          <p v-text="choicesList.row[2]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="cid"
        label="课程编号"
        align="center">
        <template slot-scope="choicesList">
          <p v-text="choicesList.row[3]"></p>
        </template>
      </el-table-column>
      <el-table-column
        prop="score"
        label="选课分数"
        align="center">
        <template slot-scope="choicesList">
          <p v-text="choicesList.row[4]"></p>
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        width="265px"
        align="center">
        <template slot-scope="choicesList">
          <el-button type="primary" icon="el-icon-view" size="mini" @click="getChoicesById(choicesList.row[0])">编辑</el-button>
          <el-button type="danger" icon="el-icon-delete" size="mini" @click="deleteChoicesById(choicesList.row[0])">删除</el-button>
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
      title="新增选课信息"
      :visible.sync="addChoicesDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>选课信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>添加选课</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 选课信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form :model="addChoicesForm">
            <el-form-item label="选课编号：" required="true">
              <el-input style="width: 800px" v-model="addChoicesForm.no"></el-input>
            </el-form-item>
            <el-form-item label="学生编号：" required="true">
              <el-input style="width: 800px" v-model="addChoicesForm.sid"></el-input>
            </el-form-item>
            <el-form-item label="教师编号：" required="true">
              <el-input style="width: 800px" v-model="addChoicesForm.tid"></el-input>
            </el-form-item>
            <el-form-item label="课程编号：" required="true">
              <el-input style="width: 800px" v-model="addChoicesForm.cid"></el-input>
            </el-form-item>
            <el-form-item label="选课分数：" required="true">
              <el-input style="width: 800px" v-model="addChoicesForm.score"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addChoicesDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addChoices()">提 交</el-button>
      </span>
    </el-dialog>
    <!-- 编辑新闻对话框 -->
    <el-dialog
      title="编辑选课信息"
      :visible.sync="updateChoicesDialogVisible"
      width="65%">
      <!-- 内容的主体区域 -->
      <!-- 面包屑导航区域 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">
          <i class="el-icon-s-home"></i>首页
        </el-breadcrumb-item>
        <el-breadcrumb-item>选课信息管理</el-breadcrumb-item>
        <el-breadcrumb-item><b>编辑选课信息</b></el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 设置分割线 -->
      <el-divider></el-divider>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-document"></i>
          <span> 选课信息</span>
        </div>
        <!-- 表单信息 -->
        <div style="margin-left: 3%">
          <el-form>
            <el-form-item label="选课编号：" required="true">
              <el-input style="width: 800px" v-model="ChoicesById[0] " disabled></el-input>
            </el-form-item>
            <el-form-item label="学生编号：">
              <el-input style="width: 800px" v-model="ChoicesById[1]"></el-input>
            </el-form-item>
            <el-form-item label="教师编号：">
              <el-input style="width: 800px" v-model="ChoicesById[2]"></el-input>
            </el-form-item>
            <el-form-item label="课程编号：">
              <el-input style="width: 800px" v-model="ChoicesById[3]"></el-input>
            </el-form-item>
            <el-form-item label="选课分数：">
               <el-input style="width: 800px" v-model="ChoicesById[4]"></el-input>
            </el-form-item>

          </el-form>
        </div>
      </el-card>
      <!-- 内容的底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="updateChoicesDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateChoices()">提 交</el-button>
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
  name: 'Choices',
  data () {
    return {
      addChoicesForm: {
        no:'',
        sid: '',
        tid: '',
        cid: '',
        score: '',
      },
      getChoicesQueryInfo: {
        query: '',
        pageSize: 5,
        pageNum: 1
      },
      getChoicesByIdInfo: {
        no: ''
      },
      updateChoicesInfo: {
        sid: '',
        tid: '',
        cid: '',
        score: ''
      },
      deleteChoicesByIdInfo: {
        no: ''
      },
      ChoicesById: {},
      ChoicesById_query: {},
      total: 0,
      choicesList: [],
      // 控制添加对话框显示与隐藏
      addChoicesDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      updateChoicesDialogVisible: false,
      // 控制编辑对话框显示与隐藏
      queryChoicesDialogVisible: false
    }
  },
  created () {
    this.getChoicesList()
  },
  methods: {
    addChoices () {
      if (this.addChoicesForm.no !== '' && this.addChoicesForm.sid !== '' && this.addChoicesForm.tid !== ''
          &&this.addChoicesForm.cid !== '' && this.addChoicesForm.score !== '') {
        // 发送请求重新修改密码
        const data = {
          no:this.addChoicesForm.no,
          sid:this.addChoicesForm.sid,
          tid:this.addChoicesForm.tid,
          cid:this.addChoicesForm.cid,
          score:this.addChoicesForm.score
        };
        axios.post('http://8.141.9.251:8080/addchoices', data)
          .then(response => {
            // 获取响应数据
            let result = response.data;
            if (result.message !== 'Choices added successfully') {
              this.$message.error(result.message);
            } else {
              this.$router.push('/choices');
              this.addChoicesDialogVisible = false;
              this.getChoicesList();
              this.$message.success(result.message);
            }
          })
          .catch(error => {
            console.error('添加选课信息时出错:', error);
            this.$message.error('添加选课信息失败');
          });
      } else {
        alert('输入有误，请重新输入！');
      }
      this.addChoicesForm = Object.assign({}, this.initialValues)
    },
    getChoicesList () {
      // 发送请求
      axios.get('http://8.141.9.251:8080/choices')
        .then(response => {
          // 获取响应数据
          let result = response.data
          if (result.choices.length ===0) {
            return this.$message.warning('获取选课列表失败!')
          } else {
            // 获取新闻列表成功
            this.pageNum = result.pageNum
            this.pageSize = result.pageSize
            this.choicesList = result.choices
            this.total = result.totalCount
          }
        })
        .catch(error => {
        this.$message.error('获取选课列表失败!')
    })
    },
    getChoicesById(no) {
      axios({
                    url: 'http://8.141.9.251:8080/choices/getchoicesById',
                    params: {
                        no: no
                    }
                })
        .then(response => {
          let result = response.data
          if (result.choice) {
            this.updateChoicesDialogVisible = true
            this.ChoicesById = result.choice
          } else {
            this.$message.error('根据选课编号获取选课信息失败!')
          }
        })
        .catch(error => {
          console.error('获取选课信息时出现错误:', error);
        });
    }
    ,
    getChoicesById_query(no) {
      axios({
                    url: 'http://8.141.9.251:8080/choices/getchoicesById',
                    params: {
                        no: no
                    }
                })
        .then(response => {
          let result = response.data
          if (result.choice) {
            this.queryChoicesDialogVisible = true
            this.ChoicesById_query = result.choice
          } else {
            this.$message.error('根据选课编号获取选课信息失败!')
          }
        })
        .catch(error => {
          console.error('获取选课信息时出现错误:', error);
        });
    }
    ,
    deleteChoicesById (no) {
      if (confirm('确定要删除吗?')) {
      axios({
                    url: 'http://8.141.9.251:8080/choices/deletechoicesById',
                    params: {
                        no:no
                    }
                })
      // axios.get(`http://localhost:8080/deletestudentsById/${sid}`)
        .then(response => {
          let result = response.data
          console.log(result)
          if (result.message === 'Choice deleted successfully') {
            this.getChoicesByIdInfo.pageNum = 1
            this.getChoicesList() 
            this.$message.success('删除选课信息成功!')
          } else {
            this.$message.error('删除选课信息失败!')
          }
        })
        .catch(error => {
          console.error('删除选课信息失败:', error)
          this.$message.error('删除选课信息失败!')
        })
    }
  },
    updateChoices () {
    //   this.updateChoicesInfo[0] = this.ChoicesById[0]
    //   this.updateChoicesInfo.sid = this.ChoicesById.sid
    //   this.updateChoicesInfo.tid = this.ChoicesById.tid
    //   this.updateChoicesInfo.cid = this.ChoicesById.cid
    //   this.updateChoicesInfo.score = this.ChoicesById.score

      const data = {
        no:this.ChoicesById[0],
        sid:this.ChoicesById[1],
        tid:this.ChoicesById[2],
        cid:this.ChoicesById[3],
        score:this.ChoicesById[4]
          
      }
      // 发送请求
      axios.post('http://8.141.9.251:8080/choices/updatechoices', data)
        .then(response => {
          // 获取响应数据
          let result = response.data
        
          if (result.message !== 'choices updated successfully') {
            return this.$message.error(result.msg)
          } else {
            this.$router.push('/choices');
            this.updateChoicesDialogVisible = false
            this.queryChoicesDialogVisible = false
            this.getChoicesList()
            this.$message.success(result.msg)
          }
        }) .catch(error => {
          console.error('编辑选课信息时出现错误:', error);
        });
    },
    handleSizeChange (newSize) {
      this.getChoicesQueryInfo.pageSize = newSize
      this.getChoicesList()
    },
    handleCurrentChange (newSize) {
      this.getChoicesQueryInfo.pageNum = newSize
      this.getChoicesList()
    },
    getChoicesByLike (newQuery) {
      this.query = newQuery
      this.getChoicesList()
    },
    getChoicesNoLike () {
      this.getChoicesQueryInfo.query = ''
      this.getChoicesList()
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
