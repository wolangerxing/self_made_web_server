# self_made_web_server
自制 Socket Web Server:自制核心 Web Server，解析/拼接原生 HTTP 报文，能够胜任后端服务器 请求/响应 需求；Model 层基于 SQL 语句自制 ORM；View 层使用 Jinja2 模板渲染；Controller 层使用 表驱动法实现路由，添加 权限验证装饰器等功能。

使用方式：

1. 环境安装：Python3 MySQL Jinja2

2. 使用方式：将 secret.py 中的 database_password 替换成你的 MySQL 数据库密码。然后运行命令
    ```
    python3 test.py
    python3 server.py
    ``` 

效果：

![demo](demo.gif)