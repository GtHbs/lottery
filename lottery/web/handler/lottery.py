import warnings

import tornado.web

from lottery.service.lottery_analysis import Analyser


class LotteryAnalysis(tornado.web.RequestHandler):

    def initialize(self, analyser: Analyser):
        self.analyser = analyser

    def get(self):
        analyse_days = self.get_argument("analyse_days", "10")
        recommend_size = self.get_argument("recommend_size", "3")
        lottery_type = self.get_argument("lottery_type", "1")
        model_type = self.get_argument("model_type", "deepseek-reasoner")
        model_brand = self.get_argument("model_brand", "deepseek")
        # self.analyser.logger.info(analyse_days, recommend_size, lottery_type, model_type)
        recommend = self.analyser.analyse(analyse_days=int(analyse_days), recommend_size=int(recommend_size),
                                          lottery_type=lottery_type, model_type=model_type, model_brand=model_brand)
        self.write(recommend)


class LotterySync(tornado.web.RequestHandler):

    def initialize(self, analyser: Analyser):
        self.analyser = analyser

    def get(self):
        pass
