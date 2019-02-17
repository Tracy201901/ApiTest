import hashlib,random


def calc_sign_md5(params_dict):
    """
    根据参数列表计算sign值
    :param params_dict: 参数列表
    :return: md5加密后的sign值
    """
    dict = params_dict
    keys = sorted(dict.keys())
    string = ""
    for key in keys:
        if dict[key] != '':
            string = string + str(key) + '=' + str(dict[key]) + '&'

    articleId = string + 'S}34546575*8wL7i'
    hash = hashlib.md5()
    hash.update(articleId.encode('utf-8'))
    return hash.hexdigest()


if __name__ == '__main__':

    dict={' uid': '20erwe158025', ' ag_fid': 'Mjzts9iUC3yiJOkF', ' register_time': '1539696956', ' nickname': 'Tlaksjd5'}
    print(calc_sign_md5(dict))

