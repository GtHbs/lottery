from pymysql.cursors import DictCursor

QWEN_API_KEY = "sk-07d5faf4aa32420b9ff76e377b3247ce"
QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL_PLUS = "qwen-plus"
DEEPSEEK_MODEL_R1 = "deepseek-r1"

LOCAL_DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "lottery_config",
    "charset": "utf8mb4",
    "cursorclass": DictCursor
}

QUERY_RECENT_PURCHASE_HISTORY_SQL = 'select * from lottery_purchase_history where lottery_type = {} and purchase_date >= (select min(purchase_date) from lottery_purchase_history order by purchase_date desc limit {});'
ANALYSIS_CONTENT = "{}： {}  {}"
ANALYSIS_CONTENT_PURCHASED = "\n\t购买了如下号码：\n{}"
ANALYSIS_NUMBER_CONTENT = "\t\t前序：{}，后序：{}"
ANALYSIS_WINNING_CONTENT = "\n\t中奖号码是：\n{}"
ANALYSIS_CONTENT_RECOMMEND_NUMBER = "{}\n以上号码为前{}期{}购买以及中奖号码，请根据以上购买以及中奖号码进行深入分析，帮我推荐{}组号码，直接给出号码，不需要额外的内容。"

LOTTERY_TYPE_1 = "超级大乐透"

LOTTERY_TYPE_DICT = {
    "1": "超级大乐透",
    "2": "双色球"
}

MODEL_DICT = {
    "1": "qwen-plus",
    "2": "deepseek-r1",
}
