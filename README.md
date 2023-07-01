# 漏洞报告辅助工具-Bug_writer

[by：逸尘]: https://github.com/yichensec/Bug_writer	"实用系列-漏洞报告辅助工具"

### 💻Bug_writer工具使用前言

本工具旨在提高渗透测试人员，和网络安全从业者，爱好者等人群的工作效率,使得更快速准确地填写更多的漏洞报告，虽然作者不是专业开发,但作为一名安全从业者，作者在用心制作这个工具来解决自己的工作需求,截至目前的公测版本,作者仅用不到8个小时完成了工具的开发的思路和优化，虽然代码逻辑有所欠缺,但未来将逐步优化。

### 🎃工具结构思路

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/000.jpg)

```cmd
Bug_writer1.0:
│
│  LICENSE
│  main.py
│  README.md
│  requirements.txt
│
├─config
│  │  WEB.docx
│  │  WEB.xlsx
│  │
│  └─漏洞模版
│          漏洞待填写模版.xlsx
│          简报模版一.docx
│          默认模板.docx
│
├─img
│      000.jpg
│      001.jpg
│      002.jpg
│      003.jpg
│      004.jpg
│      005.jpg
│      006.jpg
│      007.jpg
│
└─output
```

**📝 漏洞报告辅助工具主要由GPT智能编写，本人真不会开发，就懂一点python（注：我只是个脚本小子）**

```cmd
一款面向用于安服，渗透测试人员，网络安全从业者等人群的漏洞报告辅助工具可以生成漏洞测试简报，可自己私人定制。

当前测试版提供两个功能
1.调用本地漏洞库查询漏洞、
2.批量输出漏洞简报模版

内部版本将增加更多功能
1.半自动化填写漏洞报告（目前已实现未公布）
2.图形化GUI操作界面、
3.调用漏洞接口实时查询最新漏洞
3.批量输出正式商业用途的漏洞报告并持续更新和优化
```

### 📖 内测专版-Bug_writer 2.0

目前仅仅是做个命令行简化版本，后续打算做一个GUI图形化版本，调用某些漏洞查询的接口，实时更新 
尽请期待 Bug_writer 2.0，目前半自动化提交漏洞报告已实现，仅限内部测试中，请持续关注项目更新。

### 🏆 Bug_writer工具使用

#### 1.使用命令帮助

```
python main.py -h
```

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/001.jpg)

```
当前版本是5个参数
  -c C        指定模糊查询漏洞名称.
  -t          指定生成漏洞报告
  -list       列出漏洞名称
  -p P        指定页面数量
  -s S        指定每页显示的项目数
```

#### 2.漏洞查询

```
python main.py -c 查询漏洞(可模糊查询)
```

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/001.jpg)

```
这里设置了查询漏洞数量的记录，-c参数是指定查询漏洞名称
```

#### 3.漏洞分页展示

```
python main.py -c 未授权 -p 展示页数 -s 展示数量
```

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/003.jpg)

#### 4.漏洞简报模版生成

```
python main.py -c 漏洞名 -p 展示页数 -s 展示数量 -t 
```

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/004.jpg)

```
执行-t保存在output文件夹下的docx文件中，这里001.docx是默认名
```

#### 5.模版样式

```
打开文件夹会看到漏洞模版生成后的样式，注模板可以更换自己公司的模板
```

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/005.jpg)

#### 6.漏洞数量

```
python main.py -list 
```

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/006.jpg)

![](https://raw.githubusercontent.com/yichensec/Bug_writer/main/img/007.jpg)

### 📁 本地漏洞库漏洞报告类型

| 漏洞分类       | 漏洞名称                                        |
| -------------- | ----------------------------------------------- |
| 访问控制       | Memcached 未授权访问漏洞                        |
| 访问控制       | rsync未授权访问漏洞                             |
| 访问控制       | WebSphere绕过安全限制漏洞                       |
| 访问控制       | cisco vpn未授权访问                             |
| 访问控制       | DNS域传送漏洞                                   |
| 访问控制       | Mongodb数据库未授权访问漏洞                     |
| 访问控制       | redis数据库未授权访问漏洞                       |
| 访问控制       | phpmyadmin未授权访问                            |
| 访问控制       | .htaccess文件未授权访问                         |
| 访问控制       | 弱口令漏洞                                      |
| 访问控制       | Redis未授权访问                                 |
| 访问控制       | SprintBoot未授权访问                            |
| 访问控制       | Kibana未授权访问                                |
| 访问控制       | Druid未授权访问                                 |
| 访问控制       | Active MQ 未授权访问                            |
| 访问控制       | Atlassian Crowd 未授权访问                      |
| 访问控制       | CouchDB 未授权访问                              |
| 访问控制       | Docker 未授权访问                               |
| 访问控制       | Druid 未授权访问                                |
| 访问控制       | Elasticsearch 未授权访问                        |
| 访问控制       | FTP 未授权访问                                  |
| 访问控制       | JBoss 未授权访问                                |
| 访问控制       | Kibana 未授权访问                               |
| 访问控制       | LDAP 未授权访问                                 |
| 访问控制       | MongoDB 未授权访问                              |
| 访问控制       | NFS 未授权访问                                  |
| 访问控制       | RabbitMQ 未授权访问                             |
| 访问控制       | Solr 未授权访问                                 |
| 访问控制       | VNC 未授权访问                                  |
| 访问控制       | Weblogic 未授权访问 CVE-2020-14882              |
| 访问控制       | ZooKeeper 未授权访问                            |
| 逻辑类         | 未授权访问                                      |
| 逻辑类         | 越权漏洞                                        |
| 逻辑类         | 任意用户密码重置漏洞                            |
| 逻辑类         | 验证码漏洞                                      |
| 逻辑类         | 暴力破解漏洞                                    |
| 逻辑类         | 用户名猜解漏洞                                  |
| 逻辑类         | 短信轰炸漏洞                                    |
| 逻辑类         | 验证码可识别                                    |
| 逻辑类         | 无验证码防护                                    |
| 逻辑类         | 验证码无效                                      |
| 逻辑类         | 短信资源消耗                                    |
| 配置管理       | Struts2 dev-mod命令执行漏洞                     |
| 配置管理       | S2-005命令执行漏洞                              |
| 配置管理       | S2-009命令执行漏洞                              |
| 配置管理       | S2-016命令执行漏洞                              |
| 配置管理       | S2-017URL跳转漏洞                               |
| 配置管理       | S2-019命令执行漏洞                              |
| 配置管理       | S2-032命令执行漏洞                              |
| 配置管理       | S2-037命令执行漏洞                              |
| 配置管理       | S2-045命令执行漏洞                              |
| 配置管理       | S2-046命令执行漏洞                              |
| 配置管理       | S2-052命令执行漏洞                              |
| 配置管理       | JDWP远程命令执行漏洞                            |
| 配置管理       | ElasticSearch命令执行漏洞                       |
| 配置管理       | Resin任意文件读取漏洞                           |
| 配置管理       | GNU Bash远程命令执行                            |
| 配置管理       | Unicode 转换漏洞                                |
| 配置管理       | 检测到网站被黑痕迹                              |
| 配置管理       | 使用被弃用的SSL 2.0协议                         |
| 配置管理       | OpenSSL远程内存泄露漏洞（心脏滴血漏洞）         |
| 配置管理       | JBoss Seam参数化EL表达式远程代码执行漏洞        |
| 配置管理       | Weblogic Java反序列化远程命令执行漏洞           |
| 配置管理       | JBoss反序列化漏洞                               |
| 配置管理       | JBoss JMXInvokerServlet远程命令执行漏洞         |
| 配置管理       | Apache ActiveMQ远程代码执行漏洞 (CVE-2016-3088) |
| 配置管理       | Apache Tomcat示例目录漏洞                       |
| 配置管理       | Tomcat版本过低漏洞                              |
| 配置管理       | S2-053命令执行漏洞                              |
| 配置管理       | HPPT.sys远程代码执行漏洞（MS15-034）            |
| 配置管理       | WebDav文件上传/信息泄露漏洞                     |
| 配置管理       | slowhttp拒绝服务攻击                            |
| 配置管理       | jQuery版本过低（jQuery低版本存在跨站）          |
| 配置管理       | 不安全的javascript库文件                        |
| 配置管理       | 传输层保护不足漏洞                              |
| 配置管理       | 服务器启用了TRACE Method方法                    |
| 配置管理       | 点击劫持漏洞（X-Frame-Options头缺失）           |
| 配置管理       | 启用了不安全的HTTP方法（启用了OPTIONS方法）     |
| 配置管理       | 域名访问限制不严格                              |
| 配置管理       | 数据库弱口令                                    |
| 其它           | Webview远程代码执行漏洞                         |
| 其它           | 代码动态加载安全检测                            |
| 其它           | 应用签名未校验风险                              |
| 其它           | 篡改和二次打包风险                              |
| 其它           | Java代码反编译风险                              |
| 其它           | 资源文件泄露风险                                |
| 其它           | Webview明文存储密码风险                         |
| 其它           | 明文数字证书风险                                |
| 其它           | 应用数据任意备份风险                            |
| 其它           | AES/DES加密方法不安全使用漏洞                   |
| 其它           | 敏感函数调用风险                                |
| 其它           | HTTP传输数据风险                                |
| 其它           | HTTPS未校验服务器证书漏洞                       |
| 其它           | Activity组件导出风险                            |
| 其它           | Service组件导出风险                             |
| 其它           | Broadcast Receiver组件导出风险                  |
| 其它           | 系统组件本地拒绝服务检测                        |
| 其它           | Content Provider组件导出风险                    |
| 认证与会话管理 | SNMP默认团体名漏洞                              |
| 认证与会话管理 | FTP开启匿名登录                                 |
| 认证与会话管理 | 会话劫持漏洞                                    |
| 认证与会话管理 | 会话固定漏洞                                    |
| 认证与会话管理 | 会话cookie中缺少HttpOnly属性                    |
| 认证与会话管理 | 未禁用密码表单自动完成属性                      |
| 认证与会话管理 | 会话cookie中缺少secure属性                      |
| 认证与会话管理 | 明文传输                                        |
| 认证与会话管理 | 弱加密算法（MD5）                               |
| 认证与会话管理 | Openssh用户枚举                                 |
| 认证与会话管理 | Telnet弱口令                                    |
| 认证与会话管理 | 数据库弱口令                                    |
| 输入与输出验证 | SQL注入漏洞                                     |
| 输入与输出验证 | 存储型xss漏洞                                   |
| 输入与输出验证 | CRLF注入漏洞                                    |
| 输入与输出验证 | URL重定向钓鱼                                   |
| 输入与输出验证 | Host头攻击漏洞                                  |
| 输入与输出验证 | 框架注入漏洞                                    |
| 输入与输出验证 | CSRF跨站请求伪造漏洞                            |
| 输入与输出验证 | 文件上传漏洞                                    |
| 输入与输出验证 | 本地文件包含漏洞                                |
| 输入与输出验证 | 远程文件包含漏洞                                |
| 输入与输出验证 | SSRF（服务端请求伪造）                          |
| 输入与输出验证 | 任意文件读取漏洞                                |
| 输入与输出验证 | 任意文件下载漏洞                                |
| 输入与输出验证 | 反射型XSS                                       |
| 输入与输出验证 | XML外部实体住（XXE漏洞）                        |
| 输入与输出验证 | 命令执行                                        |
| 输入与输出验证 | 权限提升                                        |
| 输入与输出验证 | MS17-010 永恒之蓝漏洞                           |
| 输入与输出验证 | CVE-2019-0708                                   |
| 信息泄露       | SVN源代码泄露                                   |
| 信息泄露       | .idea工程目录信息泄露漏洞                       |
| 信息泄露       | ASP.NET_Padding_Oracle信息泄露(MS10-070)        |
| 信息泄露       | .git信息泄露                                    |
| 信息泄露       | 错误页面信息泄露（应用程序错误信息）            |
| 信息泄露       | 备份文件泄露                                    |
| 信息泄露       | 目录遍历                                        |
| 信息泄露       | IIS短文件名漏洞                                 |
| 信息泄露       | 源代码泄露漏洞                                  |
| 信息泄露       | robots.txt文件泄露                              |
| 信息泄露       | 敏感信息泄露                                    |
| 信息泄露       | Github信息泄露漏洞                              |
| 信息泄露       | phpinfo页面泄露                                 |
| 信息泄露       | 发现隐藏目录                                    |
| 信息泄露       | 内部IP地址泄露                                  |
| 信息泄露       | OpenSSH CBC模式信息泄露漏洞                     |
| 信息泄露       | 未加密的登录请求                                |
| 信息泄露       | Sql语句泄露                                     |
| 信息泄露       | 密码泄露                                        |
| 信息泄露       | 内网ip泄露                                      |
| 信息泄露       | Nginx版本信息泄露                               |
| 信息泄露       | Webpack源码泄露                                 |
| 信息泄露       | DS_Store文件泄漏                                |
| 信息泄露       | 敏感信息未脱敏                                  |
| 信息泄露       | Springboot信息泄露                              |

#### 👻ps：本工具目前是公开测试版本，在Github开源，未来内部版本，公布时间不定，仅优先内部团队或内部交流群使用。交流联系方式在代码中
