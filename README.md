# dictx3.0

# 简介

**dictx** :dizzy:一款偏社工属性的密码生成器，旨在使用最少最高效的字典来爆破密码，解决动辄上万、数十万密码本大量无用密码冗余，爆破数量庞大，爆破时间缓慢，对目标服务器造成拥塞等问题

支持多种密码模式生成

本脚本内置的高效精准字典，来源于多次实战积累及其他优秀工具字典参考

## 应用场景
1. 对方服务器不支持大规模登录爆破请求；
2. 知道企业域名或简称等关键词构造对应的密码；
3. 可以用户遍历遍历出存在的用户名批量为每个用户生成其对应的字典


### 自带如下类型密码：
- 常见数字弱密码 如：123、123456、111111等
- 常见用户名相关密码 如：test、test123、ceshi、ceshi123等
- 键盘习惯密码 如：1qaz@WSX、123qwe!@#、1qaz@WSX#EDC等
- 符合3原则的强密码 如：Admin@123、pass@123等

```
# 常见弱口令
weak_pass = ["admin", "test", "guest", "root", "pass", "NULL", "druid", "user", "ces", "ceshi", "tomcat", "sys",
             "system"]

# 部分强口令
strong_passwd = ["admin123", "admin@123", "admin.123", "admin#123", "admin@123", "admin888", "admin12345", "admin111",
                 "adminadmin", "admintest", "administrator", "Admin@123", "admin@1234", "Admin@1234",

                 "root123", "root@123", "ceshi123", "ceshi@123", "test123", "test@123", "Test@123",

                 "1qaz!@#$", "123qaz", "!QAZ2wsx", "1qaz!QAZ", "1qaz2wsx", "1qaz@WSX", "1!qaz2@wsx", "QAZwsx123",
                 "!QAZ3edc", "1qaz@WSX#EDC", "!QAZ@WSX#EDC", "1qaz2wsx3edc", "1234@Qaz#123",
                 "1q2w3e4r", "1234qwer", "!q2w3e4r", "2wsx#EDC", "2wsx@WSX", "QWER!@#$", "#EDC4rfv",
                 "qweasd", "qwert123", "qwert123", "qwert123", "qwe123", "qwe123456",

                 "12345qwe", "1234QWER", "1234abcd", "123456ab", "abc!@#12",

                 "pass123", "pass@123", "password", "p@ssword", "passw0rd",
                 "Pa$$w0rd", "P@ssw0rd", "P@$$word", "P@$$word123", "Passwd@123", "Passwd12",
                 "Passwd@123456", "P@ssw0rd", "P@ssw0rd!", "P2ssw0rd",

                 "aa123456", "AAss1122", "Aa123456", "123456Aa", "aaaAAA123", "a1b2c3d4",
                 "Abc123!", "Abc123!@#", "abc123", "abc123!", "abc1234!", "@bcd1234", "abc123!@#", "abcd1234",
                 "Abcd1234",
                 "abcABC123", "abcd123456789", "Abcd1234", "123123ABC"]

```



### 支持企业名称或其他关键词定制化生成字典：
- 密码等于账号
- 关键词@年份
- 关键词+@+弱口令
- 关键词(首字母大写)+@+弱口令
- 关键词#年份
- 关键词+#+弱口令
- 关键词(首字母大写)+#+弱口令
- 等等

可自定义增加、修改、删除规则


### 支持根据人名或人名列表生成字典：
人名字典的构造来自于常用弱口令加用户名的分析这里用到了姓名分词器，可自动识别姓氏、名字方便提取首字母等进行字典生成

举个栗子：

用户名：zhangwei 分解成['zhang','wei']

可能的密码(以及加上常见后缀)：
zhangwei、Zhangwei、zhangw、Zhangw、zw、Zw、ZW

zhangwei123456、zw123456、Zhangwei123456等等

此外还支持zhangw、zw这种形式用户名的字典构造

分词情况如下：
|原始用户名|分词后用户名|
|---|---|
|zhangsan|['zhangsan','Zhangsan','ZHANGsan','ZHANGSAN','zs','Zs','ZS']|
|zhangs|['zhangs','Zhangs','ZHANGSAN','zs','Zs','ZS']|
|'zs'|['zs','Zs','ZS']|

```
input: zhangsan
output:
        1、zhangsan
        2、Zhangsan
        3、ZHANGsan
        4、ZHANGSAN
        5、zs
        6、Zs
        7、ZS

input: zs
output:
        1、zs
        2、Zs
        3、ZS
    
input: zhangs
output:
        1、zhangs
        2、Zhangs
        3、ZHANGSAN
        4、zs
        5、Zs
        6、ZS
```
分词后会对新的用户名列表进行处理如加后缀等等

## 使用方法: 
`python dicx.py`

exe直接运行即可

支持如下模式：
- [x] 默认模式:不结合关键词，直接生成弱口令字典
- [x] 常规模式:结合关键词进行字典生成，字典较为精简高效如:test@2018
- [x] 单用户名模式:根据输入的用户名生成对应的密码字典
- [x] 多用户名模式:根据输入的用户名列表生成对应的用户名、密码字典

![image](https://github.com/source-xu/dictx/assets/56073532/d5535642-4a26-4912-8b7f-ce811cddfd7f)

其中模式4需要指定待生成的用户名列表，然后在当前目录下生成支持Burp **Picthfork**模式的用户名和密码字典


## 使用示例
- 【1】 默认模式  
  output：[default.txt](https://github.com/source-xu/dictx/files/11888809/default.txt)

- 【2】 常规模式，关键词：baidu  
  output：[baidu.txt](https://github.com/source-xu/dictx/files/11888833/baidu.txt)

- 【3】 单用户名模式，人名：张伟  
  output：[zhangwei.txt](https://github.com/source-xu/dictx/files/11888854/zhangwei.txt)

  
- 【4】 多用户名模式  
  input: [users.txt](https://github.com/source-xu/dictx/files/11888881/users.txt)

  output: [process_usernames.txt](https://github.com/source-xu/dictx/files/11888886/process_usernames.txt)  
         [process_passwords.txt](https://github.com/source-xu/dictx/files/11888889/process_passwords.txt)
