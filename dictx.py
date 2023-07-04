import os

from pinyintokenizer import PinyinTokenizer

banner = """
                                                    
                                          _     _   
 __  ___   _ ______ _ __   __ _ ___ ___ _| |_ _| |_ 
 \ \/ / | | |______| '_ \ / _` / __/ __|_   _|_   _|
  >  <| |_| |      | |_) | (_| \__ \__ \ |_|   |_|  
 /_/\_\\__,_|      | .__/ \__,_|___/___/            
                   | |                              
                   |_|                   V-3.0 by xu       
         """
print(banner)

# 常见数字弱密码
weak_num = ["",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "100",
            "000", "111", "222", "333", "444", "555", "666", "777", "888", "999", "1000",
            "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "10000", "00000", "11111",
            "22222", "33333", "44444", "55555", "66666", "77777", "88888", "99999", "100000",
            "000000", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999",
            "12", "123", "1234", "12345", "123456", "12345678", "1001", "5211314", "01234", "123123", "456123",
            "654321",
            "9876543210", "987654321",
            "12345678", "123456789",
            "112233", "520", "1314"]

# 常见弱口令后缀，如：damin123、admin@123、admin888
num_suffix = ["123", "1234", "1314", "12345", "123456", "123456.", "1234567", "123456789",
              "456789", "88", "888", "8888", "999999", "666", "111", "000"]

# 网址后缀
url_suffix = ["com", "cn", "org", "com.cn", "edu", "gov", "net"]

# 字符串后缀
weak_str = ["a", "aa", "aaa", "ab", "abc", "!@#", "!@#456", "qq.com"]

# 常见年份如：qq@2022
weak_year = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
             "2020", "2021", "2022", "2023", "2024", "2025"]

# 常见弱口令
weak_pass = ["admin", "test", "guest", "root", "pass", "NULL", "druid", "user", "ces", "ceshi", "tomcat", "sys",
             "system"]

# 强口令
strong_passwd = ["admin123", "admin@123", "admin.123", "admin#123", "admin@123", "admin888","Admin888s.", "admin12345", "admin111",
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

default_dict = weak_num + num_suffix + weak_year + weak_str + weak_pass + strong_passwd
dict1 = weak_num + num_suffix + weak_year + weak_str
dict2 = num_suffix + weak_year + weak_str


def weak():
    return default_dict


# 常规模式生成
def regular(keyword):
    dicts = []
    dicts.append(keyword)
    dicts = dicts + default_dict
    for i in weak_pass:
        for j in num_suffix:
            dicts.append(str(i) + str(j))
    dicts = dicts + [keyword + i for i in dict1]
    dicts = dicts + [i + keyword for i in dict1]
    dicts = dicts + [keyword.capitalize() + i for i in dict1]
    dicts = dicts + [i.capitalize() + keyword for i in dict1]
    dicts = dicts + [keyword + "@" + i for i in dict1]
    dicts = dicts + [i + "@" + keyword for i in dict1]
    dicts = dicts + [keyword.capitalize() + "@" + i for i in dict1]
    dicts = dicts + [i.capitalize() + "@" + keyword for i in dict1]
    dicts = dicts + [keyword.upper() + "@" + i for i in dict1]
    dicts = dicts + [keyword.upper() + "@" + i.upper() for i in dict1]
    dicts = dicts + [keyword + "." + i for i in dict1]
    dicts = dicts + [keyword + "#" + i for i in dict1]
    dicts = dicts + [keyword.capitalize() + i + "." for i in dict1]
    dicts = dicts + [keyword.capitalize() + i + "#" for i in dict1]
    return dicts


def processRule(m, name):
    result = m.tokenize(name)
    if len(result[0]) > 0 and len(result[1]) == 0:
        name_list = [''.join([word for word in result[0]]),
                     result[0][0].capitalize() + ''.join([word for word in result[0][1:]]),
                     result[0][0].upper() + ''.join([word for word in result[0][1:]]),
                     ''.join([word.upper() for word in result[0]]), ''.join([word[0] for word in result[0]]),
                     result[0][0] + ''.join([word[0] for word in result[0][1:]]),
                     result[0][0][0].upper() + ''.join([word[0] for word in result[0][1:]]),
                     ''.join([word[0].upper() for word in result[0]])]
        return name_list

    elif len(result[0]) > 0 and len(result[1]) > 0:
        name_list = [result[0][0] + ''.join([word for word in result[1]]),
                     result[0][0].capitalize() + ''.join([word for word in result[1]]),
                     result[0][0].upper() + ''.join([word for word in result[1]]),
                     result[0][0].upper() + ''.join([word.upper() for word in result[1]]),
                     result[0][0][0] + ''.join([word for word in result[1]]),
                     result[0][0][0].upper() + ''.join([word for word in result[1]]),
                     result[0][0][0].upper() + ''.join([word.upper() for word in result[1]])]
        return name_list
    elif len(result[0]) == 0 and len(result[1]) > 0:
        name_list = [''.join([word for word in result[1]]),
                     result[1][0].capitalize() + ''.join([word for word in result[1][1:]]),
                     ''.join([word.upper() for word in result[1]])]
        return name_list


# 用户名模式生成
def single_user(username):
    passwords = []
    m = PinyinTokenizer()
    names = processRule(m, username)
    for i in names:
        for j in num_suffix:
            passwords.append(str(i) + str(j))
    for i in default_dict:
        passwords.append(i)
    return passwords


# 用户名模式生成
def list_user(filename, mod):
    users = []
    passwords = []
    with open(filename, 'r', encoding='utf-8') as f:
        userlist = [i.strip() for i in f.readlines()]
    for rawname in userlist:
        m = PinyinTokenizer()
        names = processRule(m, rawname)
        password = set()
        for i in names:
            for j in num_suffix:
                password.add(str(i) + str(j))
        if mod == 2:
            for i in default_dict:
                password.add(i)
        passwords.extend(list(password))
        for i in range(len(list(password))):
            users.append(rawname)
    return users, passwords


def take_out_repeat(dict):
    new_dict = []
    for i in dict:
        if i not in new_dict:
            new_dict.append(i)
    return new_dict


if __name__ == '__main__':
    path = os.getcwd()
    print("""
请选择字典模式：

        【1】 默认模式:不结合关键词，直接生成弱口令字典
        【2】 常规模式:结合关键词进行字典生成，字典较为精简高效如:test@2018
        【3】 单用户名模式:根据输入的用户名生成对应的密码字典
        【4】 多用户名模式:根据输入的用户名列表生成对应的用户名、密码字典
    """)

    model = int(input("请选择模式？ 1 2 3 4:"))
    print("\n")
    if model == 1:
        dicts = weak()
        dicts = take_out_repeat(dicts)
        dicts = sorted(dicts, key=lambda i: len(i), reverse=False)
        print(f"[+] 成功生成共计{len(dicts)}条密码！！请查看！")
        with open(path + "\\" + 'default.txt', 'w') as f:
            for i in dicts:
                f.write(i + '\n')
        f.close()
    elif model == 2:
        keyword = input("请输入目标关键词: ")
        dicts = regular(keyword)
        dicts = take_out_repeat(dicts)
        dicts = sorted(dicts, key=lambda i: len(i), reverse=False)
        print(f"[+] 成功生成共计{len(dicts)}条密码！！请查看！")
        with open(path + "\\" + keyword + '.txt', 'w') as f:
            for i in dicts:
                f.write(i + '\n')
        f.close()
    elif model == 3:
        keyword = input("[*] 请输入目标关键词: ")
        dicts = single_user(keyword)
        dicts = take_out_repeat(dicts)
        dicts = sorted(dicts, key=lambda i: len(i), reverse=False)
        print(f"[+] 成功生成共计{len(dicts)}条密码！！请查看！")
        with open(path + "\\" + keyword + '.txt', 'w') as f:
            for i in dicts:
                f.write(i + '\n')
        f.close()
    elif model == 4:
        filename = input("[*] 请输入存放用户名列表文件地址：")
        print("""
    请选择生成模式：

        【1】 默认模式:根据人名生成常见弱口令，如：zhangwei123,zw123456
        【2】 全面模式:不仅包含根据人名生成的弱口令，也包含常见的弱口令如：Aa123456

        """)
        mod = int(input("请选择模式？ 1 2:"))
        print("\n")
        users, passwords = list_user(filename, mod)
        with open(path + "\\process_usernames.txt", 'w') as f:
            for i in users:
                f.write(i + '\n')
        f.close()
        with open(path + "\\process_passwords.txt", 'w') as fp:
            for i in passwords:
                fp.write(i + '\n')
        fp.close()
        print(f"[+] 成功为{len(set(users))}个用户名生成共计{len(passwords)}条密码！！请查看！")
