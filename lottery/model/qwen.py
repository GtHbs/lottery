import json

from openai.types.chat import ChatCompletion

from lottery.model.model import Model


class Qwen(Model):
    def __init__(self, api_key: str, base_url: str) -> None:
        super().__init__(api_key, base_url)

    def analyse(self, content: str, model: str):
        completion: ChatCompletion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": content},
            ],
            extra_body={"enable_thinking": True},
        )
        return completion['choices'][0]['message']['content']
