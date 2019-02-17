# 获取系统当时时间，并做相应处理后转换为时间戳
import datetime, time


def yesterday():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterdayStamp = str(int(time.mktime(yesterday.timetuple())))

    return yesterdayStamp


def tomorrow():
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    tomorrowStamp = str(int(time.mktime(tomorrow.timetuple())))
    return tomorrowStamp


if __name__ == '__main__':

    print(yesterday())
    print(tomorrow())




