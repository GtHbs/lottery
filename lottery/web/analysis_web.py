import tornado
import tornado.ioloop
import tornado.web

from lottery.service.lottery_analysis import Analyser
from lottery.web.handler.lottery import LotteryAnalysis, LotterySync
from util.util import *


def make_app():
    return tornado.web.Application([
        (r"/lotteryAnalysis", LotteryAnalysis, {"analyser": analyser}),
        (r"/lotterySync", LotterySync, {"analyser": analyser}),
    ])


if __name__ == '__main__':
    logger = LogUtil.get_logger("analysis_web")
    analyser = Analyser()
    app = make_app()
    app.listen(8888)
    logger.info("analysis_web listening on 8888")
    tornado.ioloop.IOLoop.current().start()
