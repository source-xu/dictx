import base64
import os

banner = """
                                                    
                                          _     _   
 __  ___   _ ______ _ __   __ _ ___ ___ _| |_ _| |_ 
 \ \/ / | | |______| '_ \ / _` / __/ __|_   _|_   _|
  >  <| |_| |      | |_) | (_| \__ \__ \ |_|   |_|  
 /_/\_\\__,_|      | .__/ \__,_|___/___/            
                   | |                              
                   |_|                   V-2.1 by xu       
         """
print(banner)

# 常见数字弱密码
weak_num = ["", "123123", "654321", "1001",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "100",
            "000", "111", "222", "333", "444", "555", "666", "777", "888", "999", "1000",
            "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "10000"
            "00000", "11111", "22222","33333", "44444", "55555", "66666", "77777", "88888", "99999", "100000",
            "000000", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999",
            "12", "123", "1234", "12345", "123456", "12345678", "5211314", "01234", "123123", "456123","654321","9876543210","987654321",
            "12345678", "123456789"]
# 常见弱口令后缀，如：damin123、admin@123、admin888
num_suffix = ["123", "888", "111", "12345", "123456"]
# 常见年份如：qq@2022
weak_year = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
             "2021", "2022", "2023", "2024"]
# 常见admin弱口令
weak_admin = ["admin", "admin123", "admin@123", "admin888", "admin12345", "admin111", "adminadmin", "admintest", "administrator"]
# 其他常见弱口令相关字符串
weak_str = ["root", "guest", "root123", "root@123", "user", "ceshi", "ceshi123", "ceshi@123", "test", "test123", "test@123","!@#",
            "pass", "pass123", "pass@123", "password", "p@ssword", "passw0rd", "NULL", "tomcat", "sys", "system", "qq.com"
            ]
# 强口令
strong_passwd = ["aa123456", "Aa123456", "Abc123!", "Abc123!@#", "abc123", "abc123!", "abc1234!", "@bcd1234",
                 "abc123!@#", "Abc123!@#", "#EDC4rfv", "abcABC123", "1qaz!@#$", "admin@123", "Admin@123", "admin@1234",
                 "Admin@1234", "QAZwsx123", "Pa$$w0rd", "P@ssw0rd", "P@$$word", "P@$$word123", "Abcd1234", "!QAZ2wsx",
                 "qwe123", "!QAZ3edc", "2wsx#EDC", "123qaz", "1!qaz2@wsx", "1q2w3e4r", "1234abcd", "1234qwer", "1qaz!QAZ", "1qaz2wsx",
                 "1qaz@WSX", "1qaz@WSX#EDC", "qweasd", "!q2w3e4r", "1234qwer", "1234QWER", "QWER!@#$", "Passwd@123", "Passwd12",
                 "Passwd@123456", "P@ssw0rd", "P@ssw0rd!", "!QAZ@WSX#EDC", "p@ssw0rd", "P2ssw0rd", "1qaz2wsx3edc",
                 "abcd123456789", "123456Aa", "Abcd1234", "1234@Qaz#123"]


default_dict = weak_num + weak_year + weak_admin + weak_str + strong_passwd
edit_dict1 = num_suffix + weak_year + weak_admin
edit_dict2 = weak_num + weak_year + weak_admin


# 默认161个字典
def weak():
    return default_dict


# 常规模式生成
def regular(keyword):
    dicts = []
    dicts.append(keyword)
    dicts = dicts + default_dict
    dicts = dicts + [keyword + i for i in edit_dict1]
    dicts = dicts + [i + keyword for i in edit_dict1]
    dicts = dicts + [keyword.capitalize() + i for i in edit_dict1]
    dicts = dicts + [i.capitalize() + keyword for i in edit_dict1]
    dicts = dicts + [keyword + "@" + i for i in edit_dict1]
    dicts = dicts + [i + "@" + keyword for i in edit_dict1]
    dicts = dicts + [keyword.capitalize() + "@" + i for i in edit_dict1]
    dicts = dicts + [i.capitalize() + "@" + keyword for i in edit_dict1]
    dicts = dicts + [keyword.upper() + "@" + i for i in edit_dict1]
    dicts = dicts + [keyword.upper() + "@" + i.upper() for i in edit_dict1]
    dicts = dicts + [keyword + "." + i for i in edit_dict1]
    dicts = dicts + [keyword + "#" + i for i in edit_dict1]
    dicts = dicts + [keyword.capitalize() + i + "." for i in edit_dict1]
    dicts = dicts + [keyword.capitalize() + i + "#" for i in edit_dict1]
    return dicts


# 全面模式将生成515条字典
def overall(keyword):
    dicts = []
    dicts = dicts + default_dict
    dicts = dicts + [keyword + i for i in edit_dict2]
    dicts = dicts + [i + keyword for i in edit_dict2]
    dicts = dicts + [keyword.capitalize() + i for i in edit_dict2]
    dicts = dicts + [i.capitalize() + keyword for i in edit_dict2]
    dicts = dicts + [keyword.upper() + i for i in edit_dict2]
    dicts = dicts + [i.upper() + keyword for i in edit_dict2]
    dicts = dicts + [keyword.upper() + i.upper() for i in edit_dict2]
    dicts = dicts + [keyword + "@" + i for i in edit_dict2]
    dicts = dicts + [keyword + "@" + i + "." for i in edit_dict2]
    dicts = dicts + [i + "@" + keyword for i in edit_dict2]
    dicts = dicts + [keyword.capitalize() + "@" + i for i in edit_dict2]
    dicts = dicts + [keyword.capitalize() + "@" + i + "." for i in edit_dict2]
    dicts = dicts + [i.capitalize() + "@" + keyword for i in edit_dict2]
    dicts = dicts + [keyword.upper() + "@" + i for i in edit_dict2]
    dicts = dicts + [i.upper() + "@" + keyword for i in edit_dict2]
    dicts = dicts + [keyword.capitalize() + "@" + i for i in weak_year]
    dicts = dicts + [keyword.upper() + "@" + i.upper() for i in edit_dict2]
    dicts = dicts + [keyword + "." + i for i in edit_dict2]
    dicts = dicts + [keyword + "#" + i for i in edit_dict2]
    dicts = dicts + [keyword.capitalize() + i + "." for i in edit_dict2]
    dicts = dicts + [keyword.capitalize() + i + "#" for i in edit_dict2]
    dicts.append(keyword)
    dicts.append(keyword+".")
    dicts.append(keyword + "..")
    dicts.append(keyword + "...")
    return dicts


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

        【1】 默认模式(176条):不结合关键词，直接生成弱口令字典
        【2】 常规模式(556条):结合关键词进行字典生成，字典较为精简高效如:test@2018
        【3】 全面模式(1701条):结合关键词进行字典生成，支持复杂得规则如Test@123.
    """)

    model = int(input("请选择模式？ 1 2 3: "))
    if model == 1:
        dicts = weak()
        dicts = take_out_repeat(dicts)
        dicts = sorted(dicts, key=lambda i: len(i), reverse=False)
        print(len(dicts))
        with open(path + "\\" + 'default.txt', 'w') as f:
            for i in dicts:
                f.write(i + '\n')
        f.close()
    elif model == 2:
        keyword = input("请输入目标关键词: ")
        dicts = regular(keyword)
        dicts = take_out_repeat(dicts)
        dicts = sorted(dicts, key=lambda i: len(i), reverse=False)
        print(len(dicts))
        with open(path + "\\" + keyword + '.txt', 'w') as f:
            for i in dicts:
                f.write(i + '\n')
        f.close()
    else:
        keyword = input("请输入目标关键词: ")
        dicts = overall(keyword)
        dicts = take_out_repeat(dicts)
        dicts = sorted(dicts, key=lambda i: len(i), reverse=False)
        print(len(dicts))
        with open(path + "\\" + keyword + '.txt', 'w') as f:
            for i in dicts:
                f.write(i + '\n')
        f.close()
    print("共生成{}条密码！！请查看！".format(len(dicts)))



