# SnowField 雪原
Python代码静态漏洞扫描器

[toc]

## 扫描器结构设计

扫描器由六个组件构成：

- cfgEngine：负责从抽象语法树构建控制流图
- fixEngine：预置一些对扫描出的风险点去风险的解决方案
- logEngine：提供有不同特性的log函数，如控制台log，文件log，邮箱提醒扫描结果等
- moduleEngine：python以module为单位组织程序，扫描器也以module为单位构建控制流图，moduleEngine即是负责提供module建模，模型存储以及扫描时的模型导入等的功能
- scanEngine：负责根据控制流图进行污点追踪
- testEngine：集成开发中需要的测试功能，记录测试结果以便于扫描器迭代开发

## 抽象语法树的生成

我的扫描器使用python内置的库ast来生成抽象语法树，抽象语法树的各类细节参考官方文档：https://docs.python.org/3/library/ast.html

## 控制流图的构建

