from util.settings import *
from util.qwen_util import *
from util.util import *


class Analyser:
    def __init__(self):
        self.helper = MySQLHelper(LOCAL_DB_CONFIG)
        self.logger = LogUtil.get_logger("analyser")

    @staticmethod
    def struct_content(purchase_histories: list) -> list:
        purchase_dict = {}
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
        analysis_list = []
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

    """
    @:param analyse_days 分析天数
    """

    def analyse(self, analyse_days: int, recommend_size: int, lottery_type: str, model_type: str) -> str:
        sql = QUERY_RECENT_PURCHASE_HISTORY_SQL.format("'" + LOTTERY_TYPE_DICT[lottery_type] + "'", analyse_days)
        self.logger.info("query sql: %s" % sql)
        purchase_histories = self.helper.execute_query(sql)
        analysis_list = self.struct_content(purchase_histories)
        self.logger.info("analysis_list: %s" % json.dumps(analysis_list, ensure_ascii=False))
        if not analysis_list:
            raise Exception("数据为空，退出本次分析")
        analysis_content = ANALYSIS_CONTENT_RECOMMEND_NUMBER.format("\n".join(analysis_list), analyse_days,
                                                                    LOTTERY_TYPE_DICT[lottery_type],
                                                                    recommend_size)
        self.logger.info("analysis_content: %s" % analysis_content)
        qwen = Qwen(api_key=QWEN_API_KEY, base_url=QWEN_BASE_URL)
        analysis_result = qwen.analyse(content=analysis_content, model=MODEL_DICT[model_type])
        self.logger.info("analysis_result: %s" % analysis_result)
        recommend = analysis_result['choices'][0]['message']['content']
        return recommend
