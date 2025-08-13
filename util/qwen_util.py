import json

from openai.types.chat import ChatCompletion

from openai import *


class Qwen:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.client = self.init_client()

    def init_client(self):
        return OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def analyse(self, content: str, model: str):
        completion: ChatCompletion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": content},
            ],
            extra_body={"enable_thinking": False},
        )
        return json.loads(completion.model_dump_json())
