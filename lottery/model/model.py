from openai import OpenAI


class Model:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.client = self.init_client()

    def init_client(self) -> OpenAI:
        return OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def analyse(self, content: str, model: str) -> str:
        pass
