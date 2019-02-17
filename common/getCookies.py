"""
从txt文件中读取cookie数据并转化成字典
"""



def Cookies():

    cookies_dict = {}
    #从text文件读取cookie信息
    with open('/Users/tracy/PycharmProjects/ApiTest/data/cookies_tracy') as f:
        cookies = f.read()

        for line in cookies.split(';'):
            key,value = line.split('=', 1)
            cookies_dict[key]=value

    return cookies_dict


if __name__ == '__main__':

    print(Cookies())
