"""
使用requets库请求服务器数据
2019年2月17日 by tracy
"""
import unittest
import requests



class NetworkTest(unittest.TestCase):

    bas_url = 'https://api.douban.com/v2/'

    def test_http_get_by_path(self, path, params=None, headers=None):
        """
        向服务器发起get请求，得到返回结果
        :param path:  请求 path
        :param params: 请求参数
        :param headers: 请求headers
        :return:  返回status_code和解析后的json文件
        """
        try:
            req = requests.get(url=(self.bas_url + path), params=params, headers=headers)
            print(req.url)
            self.assertEqual(req.status_code, 200, '服务器异常，status_code不等于200')
            return req.json()
        except:
            assert False

    def test_http_get_by_url(self, url, params=None, headers=None):
        """
        向服务器发起get请求，得到返回结果
        :param path:  请求 path
        :param params: 请求参数
        :param headers: 请求headers
        :return:  返回status_code和解析后的json文件
        """
        try:
            req = requests.get(url, params=params, headers=headers)
            self.assertEqual(req.status_code, 200, '服务器异常，status_code不等于200')
            print(req.url)
            return req.json()
        except:
            assert False


if __name__ == '__main__':

    tag = '科幻'
    params = dict(tag=tag)
    network = NetworkTest()





