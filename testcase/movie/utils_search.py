

class UtilsSearch():
    """对搜索结果进行校验"""

    def check_total(self, total, keyword):
        """判断title中是否包含搜索关键字"""
        for iterm in total:
            if keyword in iterm:
                return True
        return False

    def check_result(self, subject, keyword):
        """校验搜索结果的电影名字、主要演员、导演名字中包含搜索关键字"""

        title = [subject['title']]
        casts = [i['name'] for i in subject['casts']]
        directors = [i['name'] for i in subject['directors']]
        total = title + casts + directors  #将电影名字、主要演员、导演名字放入total中

        print('关键字', keyword, '搜索结果：', total)

        return self.check_total(total, keyword)

    def check_tags(self, subject, keyword):
        """校验搜索结果的tags中是否包含搜索关键字"""

        generes = subject.get('genres')
        print('关键字', keyword, '搜索结果：', generes)

        return self.check_total(generes, keyword)






