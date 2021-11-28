from datetime import datetime
from app import pity
from app.utils.logger import Log

@pity.route('/')
def hello_world():
    log = Log("hello world")
    log.info("有人访问了你的网站了")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    return now


if __name__ == '__main__':
    pity.run()
