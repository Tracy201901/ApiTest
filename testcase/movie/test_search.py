"""
2019年1月4日下午，在涛神的帮助下，确定自动化接口测试代码包结构，完成豆瓣搜索用例编写
"""

import unittest
from testcase.test_request.test_request import NetworkTest
from testcase.movie.utils_search import UtilsSearch


class TestMovieSearch(unittest.TestCase):
    """测试豆瓣电影搜索接口（与图片编辑页搜索贴纸类似）"""

    path = 'movie/search'

    def setUp(self):
        print('开始执行用例')
        self.network = NetworkTest()
        self.utilsSearch = UtilsSearch()
        self.network = NetworkTest()

    def tearDown(self):
        print('用例执行完成')

    def test_a_search_by_name(self):
        """通过演员或电影名字来搜索"""

        names = ['刘亦菲', '赵丽颖', '芳华', '无问西东', '平行宇宙', '三块广告牌', '鲍勃']
        for name in names:
            params = dict(q=name)
            req = self.network.test_http_get_by_path(self.path, params)
            subjects = req.get('subjects')
            self.assertTrue(len(subjects) > 0, '搜索结果为空')
            self.assertTrue(self.utilsSearch.check_result(subjects[0], name), '第一条搜索结果不包含关键字')

    def test_b_search_by_tags(self):
        """通过影片分类来搜索"""

        tags = ['科幻', '喜剧', '剧情', '动作']
        for tag in tags:
            params = dict(tag=tag)
            req = self.network.test_http_get_by_path(self.path, params)
            subjects = req.get('subjects')
            self.assertTrue(len(subjects) > 0, '搜索结果为空')
            self.assertTrue(self.utilsSearch.check_tags(subjects[0], tag), '第一条搜索结果不包含关键字')

    def test_c_search_by_special_word(self):
        """搜索特殊字符、超长字符，结果为空"""

        names = ['科幻fwehvohvohdouvhoudsbvcuwbvuwrguowhugohwoergh2397489', '', '#$$%%^%', '23534']
        for name in names:
            params = dict(q=name)
            req = self.network.test_http_get_by_path(self.path, params)
            self.assertTrue(len(req.get('subjects'))==0)
            print('关键字', name, '搜索结果为空')

    def test_d_search_without_params(self):
        """没有添加参数都时候，服务器返回结果为空"""
        req = self.network.test_http_get_by_path(self.path)
        self.assertTrue(len(req.get('subjects')) == 0)








