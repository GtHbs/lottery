import json

from util.settings import *
from util.util import *


class Lottery:
    def __init__(self, analyse_days: int, recommend_size: int, lottery_type: str):
        self.logger = LogUtil.get_logger("Lottery")
        self.analyse_days = analyse_days
        self.recommend_size = recommend_size
        self.lottery_type = lottery_type

    def struct_content(self, purchase_histories: list) -> list:
        # self.logger.info("Lottery.struct_content's param: {}".format(json.dumps(purchase_histories)))

        purchase_dict = dict()
        for purchase_history in purchase_histories:
            purchase_date = purchase_history['purchase_date']
            detail = {
                "purchase_number_pre": purchase_history['purchase_number_pre'],
                "purchase_number_post": purchase_history['purchase_number_post'],
                "winning_number_pre": purchase_history['winning_number_pre'],
                "winning_number_post": purchase_history['winning_number_post']
            }
            if purchase_date in purchase_dict.keys():
                purchase_dict[purchase_date].append(detail)
            else:
                purchase_dict[purchase_date] = [detail]
        analysis_list = list()
        for purchase_date, details in purchase_dict.items():
            whether_purchase = False
            purchased_list = []
            winning_list = []
            for detail in details:
                purchase_number_pre = detail['purchase_number_pre']
                purchase_number_post = detail['purchase_number_post']
                winning_number_pre = detail['winning_number_pre']
                winning_number_post = detail['winning_number_post']
                if purchase_number_pre is not None and purchase_number_post is not None:
                    whether_purchase = True
                    purchased_number = ANALYSIS_NUMBER_CONTENT.format(purchase_number_pre, purchase_number_post)
                    purchased_list.append(purchased_number)
                winning_number = ANALYSIS_NUMBER_CONTENT.format(winning_number_pre, winning_number_post)
                winning_list.append(winning_number)

            winning = ANALYSIS_WINNING_CONTENT.format(winning_list[0])
            if whether_purchase:
                purchased = ANALYSIS_CONTENT_PURCHASED.format("\n".join(purchased_list))
                analysis_content = ANALYSIS_CONTENT.format(purchase_date, purchased, winning)
            else:
                analysis_content = ANALYSIS_CONTENT.format(purchase_date, " ", winning)
            analysis_list.append(analysis_content)
        return analysis_list

    def get_analysis_content(self, purchase_histories: list) -> str:
        analysis_list: list = self.struct_content(purchase_histories)
        if not analysis_list:
            raise Exception("数据为空")
        analysis_content = ANALYSIS_CONTENT_RECOMMEND_NUMBER.format("\n".join(analysis_list), self.analyse_days,
                                                                    LOTTERY_TYPE_DICT[self.lottery_type],
                                                                    self.recommend_size)
        self.logger.info("analysis_content: %s" % analysis_content)
        return analysis_content
