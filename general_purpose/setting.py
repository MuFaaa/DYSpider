# redis数据库

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
STARTBODY = 1773

# 设置下载延迟
DOWNLOAD_DELAY = 3
# 设置随机ip
PROXIES = False
# 设置每秒请求次数，并发量，数字越大越快
CONCURRENCE = 32

# 是否往数据库添加文档,默认文档名为查询国内货型号NOP8.csv
STARTCSV = True

# 以下所有功能，都需根据需要单独开启，不可开启多个，True为开启，False为关闭

# 是否启动web爬虫，默认开启
WEBSTART = False

# 是否启动web未发现的id重新爬取，需单独开启
WEBNOTFID = True

# 是否启动web出现验证码的id重新爬取，需单独开启
WEBVERIFICATION = False

# 是否启动h5爬虫，默认关闭，WEBSTART和H5START不可同时开启。
H5START = False

# 是否启动H5未发现的id重新爬取，需单独开启
H5NOTFID = False

# 是否启动H5出现验证码的id重新爬取，需单独开启
H5VERIFICATION = False
