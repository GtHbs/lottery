from openai import OpenAI

from lottery.model.model import Model


class DeepSeek(Model):
    def __init__(self, api_key: str, base_url: str) -> None:
        super().__init__(api_key, base_url)

    def analyse(self, content: str, model: str) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": content},
            ],
            stream=False
        )
        return response.choices[0].message.content