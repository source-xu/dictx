# dictx
渗透测试根据企业名称或其他关键词定制化生成字典，旨在最少的请求数碰撞密码

本脚本内置高效精准的字典，来源于多次实战积累及其他优秀工具字典参考

最可自定义增加、修改、删除规则

**usage: `python dicx.py`**


### 支持如下类型密码：
【1】常见数字弱密码

【2】Admin相关密码

【3】年份相关密码

【4】常见用户名相关密码

【5】符合3原则的强密码


### 支持如下模式（以test为例）：
【1】 默认模式(176条):不结合关键词，直接生成弱口令字典

【2】 常规模式(556条):结合关键词进行字典生成，字典较为精简高效如:test@2018

【3】 全面模式(1701条):结合关键词进行字典生成，支持复杂得规则如Test@123.

