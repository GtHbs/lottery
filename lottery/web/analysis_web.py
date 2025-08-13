import tornado
import tornado.ioloop
import tornado.web

from lottery.service.lottery_analysis import *
from util.util import *


class LotteryAnalysis(tornado.web.RequestHandler):
    def get(self):
        analyse_days = self.get_argument("analyse_days", "10")
        recommend_size = self.get_argument("recommend_size", "3")
        lottery_type = self.get_argument("lottery_type", "1")
        model_type = self.get_argument("model_type", "1")
        logger.info(analyse_days, recommend_size, lottery_type, model_type)
        recommend = analyser.analyse(analyse_days=int(analyse_days), recommend_size=int(recommend_size),
                                     lottery_type=lottery_type, model_type=model_type)
        self.write(recommend)


def make_app():
    return tornado.web.Application([
        (r"/lotteryAnalysis", LotteryAnalysis),
    ])


if __name__ == '__main__':
    logger = LogUtil.get_logger("analysis_web")
    analyser = Analyser()
    app = make_app()
    app.listen(8888)
    logger.info("analysis_web listening on 8888")
    tornado.ioloop.IOLoop.current().start()
