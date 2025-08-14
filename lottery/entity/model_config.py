from lottery.model.deepseek import DeepSeek
from lottery.model.model import Model
from lottery.model.qwen import Qwen


class MultiModel:
    def __init__(self, brand: str, model_name: str, api_key: str, base_url: str):
        self.brand = brand
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url

    def analyse(self, content: str) -> str:
        model: Model = None
        if self.brand == "deepseek":
            model = DeepSeek(api_key=self.api_key, base_url=self.base_url)
        if self.brand == "qwen":
            model = Qwen(api_key=self.api_key, base_url=self.base_url)
        if model is None:
            raise Exception("模型初始化失败")
        return model.analyse(content, self.model_name)
