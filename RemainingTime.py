from datetime import datetime, date

dd = '2024-09-30'
dd = datetime.strptime(dd, "%Y-%m-%d").date()
d_now = date.today()
days = (dd - d_now).days


if __name__ == '__main__':
    print(days)
    input("按下回车关闭页面")
    # timeStamp = 1639533600
    # dateArray = datetime.utcfromtimestamp(timeStamp)
    # otherStyleTime = dateArray.strftime("%Y/%m/%d %H:%M:%S")
    # print(otherStyleTime)