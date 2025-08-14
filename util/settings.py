from pymysql.cursors import DictCursor

LOCAL_DB_CONFIG = {
    "host": "106.13.34.98",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "lottery_config",
    "charset": "utf8mb4",
    "cursorclass": DictCursor
}

QUERY_RECENT_PURCHASE_HISTORY_SQL = 'select * from lottery_purchase_history where lottery_type = {} and purchase_date >= (select min(purchase_date) from lottery_purchase_history order by purchase_date desc limit {});'
QUERY_MODEL_SQL = "select * from multi_model.model_config where brand = {} and model_name = {} and is_deleted = 0;"
ANALYSIS_CONTENT = "{}： {}  {}"
ANALYSIS_CONTENT_PURCHASED = "\n\t购买了如下号码：\n{}"
ANALYSIS_NUMBER_CONTENT = "\t\t前序：{}，后序：{}"
ANALYSIS_WINNING_CONTENT = "\n\t中奖号码是：\n{}"
ANALYSIS_CONTENT_RECOMMEND_NUMBER = "{}\n以上号码为前{}期{}购买以及中奖号码，请根据以上购买以及中奖号码进行深入分析，帮我推荐{}组号码，直接给出号码，不需要额外的内容。"


LOTTERY_TYPE_DICT = {
    "1": "超级大乐透",
    "2": "双色球"
}
