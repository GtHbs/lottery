from lottery.entity.model_config import *
from lottery.entity.lottery import *


class Analyser:
    def __init__(self):
        self.helper = MySQLHelper(LOCAL_DB_CONFIG)
        self.logger = LogUtil.get_logger("analyser")

    def query_models(self, model_type: str, model_brand: str) -> MultiModel:
        query_model_sql = QUERY_MODEL_SQL.format("'" + model_brand + "'", "'" + model_type + "'")
        model_config = self.helper.execute_query(query_model_sql)
        if not model_config:
            raise Exception("模型不存在")
        model_config = model_config[0]
        brand = model_config['brand']
        model_name = model_config['model_name']
        api_key = model_config['model_api_key']
        base_url = model_config['model_base_url']
        multi_model = MultiModel(brand=brand, model_name=model_name, api_key=api_key, base_url=base_url)
        # self.logger.info("multi_model: %s" % json.dumps(multi_model, ensure_ascii=False))
        return multi_model

    def query_purchase_history(self, analyse_days: int, recommend_size: int, lottery_type: str) -> str:
        sql = QUERY_RECENT_PURCHASE_HISTORY_SQL.format("'" + LOTTERY_TYPE_DICT[lottery_type] + "'", analyse_days)
        self.logger.info("query sql: %s" % sql)
        purchase_histories = self.helper.execute_query(sql)
        lottery = Lottery(analyse_days=analyse_days, recommend_size=recommend_size, lottery_type=lottery_type)
        return lottery.get_analysis_content(purchase_histories=purchase_histories)

    """
    @:param analyse_days 分析天数
    """

    def analyse(self, analyse_days: int, recommend_size: int, lottery_type: str, model_type: str,
                model_brand: str) -> str:
        multi_model: MultiModel = self.query_models(model_type=model_type, model_brand=model_brand)
        analysis_content = self.query_purchase_history(analyse_days=analyse_days, recommend_size=recommend_size,
                                                       lottery_type=lottery_type)
        recommend = multi_model.analyse(content=analysis_content)
        self.logger.info("分析结果：{}".format(json.dumps(recommend, ensure_ascii=False)))
        return recommend
