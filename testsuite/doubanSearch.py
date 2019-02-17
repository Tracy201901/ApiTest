import HTMLTestRunner, time, unittest
from testcase.movie.test_search import TestMovieSearch

if __name__ == '__main__':
    doubanmovieSearch = unittest.TestLoader().loadTestsFromTestCase(TestMovieSearch)
    suitePic = unittest.TestSuite([doubanmovieSearch])

    now = time.strftime("%y-%m-%d %X", time.localtime((time.time())))
    report_file_path = "/Users/tracy/PycharmProjects/ApiTest/report/"  # 定义个报告存放路径，支持相对路径，将文件名后加上日期
    filename = report_file_path + '豆瓣电影搜索接口测试报告' + now + ".html"

    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="豆瓣电影搜索接口测试报告", description="详细内容")
        runner.run(suitePic)



